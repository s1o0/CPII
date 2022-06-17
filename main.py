from osgeo import gdal,osr,ogr
import os
from parse_folder import parse_folder
from getName_ign import getName
from percent import percent_black

path_to_ign = "./29_Ortho_IGN_2021/Littoral/"
files = os.listdir(path_to_ign)

path_to_pleiade_reproj = "./Images_reproj/"
files2 = os.listdir(path_to_pleiade_reproj)
#Ajouter la variable pour turn sur le i
i =1
x = 1
while i<= 424:
    print()
    #os.system(f'mkdir ./tuiles/{i}/')
    os.system(f'mkdir ./result/{i}/')
    os.system(f'ogr2ogr -where ID={i} ./result/{i}/tuile.shp {path_to_ign}/dalles/dalles.shp')
    nom_fichier = getName(f'./result/{i}/tuile.shp')
    nom_fichier = nom_fichier[2:]
    if nom_fichier in files:
        u = 1
        for img in files2:
            os.system(f'mkdir ./result/{i}/{u}/')
            os.system(f'gdalwarp -cutline ./result/{i}/tuile.shp -crop_to_cutline ./Images_reproj/{img} ./result2/pleiade/{x}.tif')
            #os.system(f'cp {path_to_pleiade_reproj}/{img} ./result/{i}/{u}/{img}')
            nom = getName(f'./result/{i}/tuile.shp')
            nom = nom[2:]
            #os.system(f'cp {path_to_ign}/{nom} ./result/{i}/{u}/{nom}')
            percent = percent_black(f'./result2/pleiade/{x}.tif')
            print()
            print(f'Le pourcentage de cette image est de : {percent}')
            if percent <76.0:
                os.system(f'cp {path_to_ign}/{nom} ./result2/ign/{x}.jp2')
                #os.system(f'cp ./result/{i}/{u}/OUTPUT.tif ./result2/pleiade/{x}.tif')
            else:
                os.system(f'rm ./result2/pleiade/{x}.tif')
            u += 1 
            x += 1
    else:
        print(f'Nous ne possédons pas le fichier ign en question : {i}')
        print()
    #os.system(f'rm -r ./result/{i}/')
    i+=1
    
    
print("Done")
    


