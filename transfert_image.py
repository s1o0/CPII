from osgeo import gdal
import os
from parse_folder import parse_folder
#Objectif : Générer des images Pleiades dans le dossier Images_reproj en fonction de leurs fichiers DIM.
#Prérequis : Python, GDAL. Il faut également lister tous les fichiers DIM dans un fichier x.txt (Voir documentation "Github - Découpe des PLEIADES")

#On ouvre le fichier x.txt en mode lecture
x = open('./x.txt','r')
i = 1 
for lines in x:
    #On supprime les retours chariots
    line = lines.strip()
    #Première exécution d'une méthode GDAL pour générer une image PLEIADES dans le dossier Img_DIM en fonction du fichier DIM 
    os.system(f'gdal_translate -of GTiff -co COMPRESS=NONE -co BIGTIFF=IF_NEEDED {line} ./Img_Dim/{i}.tif')
    #Deuxième exécution d'une méthode GDAL pour reprojeter l'image GDAL dans le format EPSG:2154 
    os.system(f'gdal_translate -a_srs EPSG:2154 -ot UInt16 -of GTiff ./Img_Dim/{i}.tif ./Images_reproj/{i}.tif')
    i+=1 
print("done")
	
#A NOTER :
#Si vous le souhaitez vous pouvez écrire cette ligne en fin de script pour supprimer le contenu du dossier Img_Dim pour libérer de la place :
#os.system(rm -r ./Img_Dim/)


