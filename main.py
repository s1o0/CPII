from osgeo import gdal,osr,ogr
import os
from parse_folder import parse_folder
from getName_ign import getName
from percent import percent_black
#Objectif : C'est le script principal de cette partie du projet. Son but va être de boucler sur les tuiles pour couper chacunes des images PLEIADES et ensuite les supprimer ou les garder en fonction du % de nodata qu'elles possèdent
#Prérequis : GDAL, getName_ign.py, percent.py.
#/!\ ATTENTION /!\ : L'exécution de ce script est assez longue et peut prendre plusieurs heures/jours en fonction du nombre d'images PLEIADES.

#Chemin vers le dossier contenant les images aériennes IGN. IL EST TRES IMPORTANT QUE CE CHEMIN MENE AU DOSSIER LITTORAL car ce dossier contient les images IGN + les dossiers "dalles"
#Ce chemin est à changer en fonction de votre contexte d'utilisation comme indiqué sur le document pdf "Github - Découpes des PLEIADES"
path_to_ign = "./29_Ortho_IGN_2021/Littoral/"
files = os.listdir(path_to_ign)

path_to_pleiade_reproj = "./Images_reproj/"
files2 = os.listdir(path_to_pleiade_reproj)

i =1
x = 1
#La valeur sur laquelle la variable i doit boucler correspond au nombre de dalles présentes sur ces zones.
while i<= 424:
    print()
    os.system(f'mkdir ./result/{i}/')
    #Exécution de la méthode ogr2ogr pour pouvoir récupérer la tuile en fonction de son ID
    os.system(f'ogr2ogr -where ID={i} ./result/{i}/tuile.shp {path_to_ign}/dalles/dalles.shp')
    #On récupérer le nom de l'image IGN correspondante à cette tuile
    nom_fichier = getName(f'./result/{i}/tuile.shp')
    nom_fichier = nom_fichier[2:]
    #Si on possède cette image dans nos dossiers......
    if nom_fichier in files:
        u = 1
        #On boucle sur toutes les images PLEIADES
        for img in files2:
            os.system(f'mkdir ./result/{i}/{u}/')
            #On va couper à l'aide de GDAL l'image PLEIADE en fonction de la tuile. Le résultat se trouvera dans le répertoire "result2/pleiade/"
            os.system(f'gdalwarp -cutline ./result/{i}/tuile.shp -crop_to_cutline ./Images_reproj/{img} ./result2/pleiade/{x}.tif')

            ###os.system(f'cp {path_to_pleiade_reproj}/{img} ./result/{i}/{u}/{img}')

            nom = getName(f'./result/{i}/tuile.shp')
            nom = nom[2:]

            ###os.system(f'cp {path_to_ign}/{nom} ./result/{i}/{u}/{nom}')

            #On calcule le pourcentage de nodata présents sur l'image découpée
            percent = percent_black(f'./result2/pleiade/{x}.tif')
            print()
            print(f'Le pourcentage de cette image est de : {percent}')
            #Si ce pourcentag est inférieur à 76%, alors on garde l'image et on copie-colle l'image IGN correspondante dans le dossier result2/ign/
            if percent <76.0:
                os.system(f'cp {path_to_ign}/{nom} ./result2/ign/{x}.jp2')

                ###os.system(f'cp ./result/{i}/{u}/OUTPUT.tif ./result2/pleiade/{x}.tif')

            #Si l'image possède + de 76% de nodata alors on la supprime
            else:
                os.system(f'rm ./result2/pleiade/{x}.tif')
            u += 1 
            x += 1
    #Si on ne possède pas cette image dans nos dossiers....
    else:
        print(f'Nous ne possédons pas le fichier ign en question : {i}')
        print()

    ###os.system(f'rm -r ./result/{i}/')

    i+=1
print("Done")
    
#/!\ ATTENTION : Les lignes commençant par "#" sont de la documentation, alors que les lignes commençant par "###" sont des lignes de codes qui sont juste mises en commentaires car elles peuvent servir pour un debuggage de l'algorithme


