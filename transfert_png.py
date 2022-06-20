import os 
#Objectif : Le but de ce script est de transformer les images PLEIADES découpées et leur équivalent IGN au format .PNG avec des pixels en Uint8 ( 0 - 255 de plage de valeurs)
#Prérequis : Python, GDAL.

#Chemin vers les images que vous souhaitez transformer
x = os.listdir('./result2/pleiade/')
#Index servant à nommer les images 
y = 93
for file in x:
    #Première exécution de gdal_translate pour transformer l'image PLEIADES au format voulu. le résultat se produit dans le dossier "./final/pleiade/"
    os.system(f'gdal_translate -ot Byte -of PNG -b 1 -b 2 -b 3 -scale ./result2/pleiade/{file} ./final/pleiade/{y}.PNG')
    #Deuxième exécution de gdal_translate pour transformer l'image IGN correspondante au format voulu. le résultat se produit dans le dossier "./final/pleiade/"
    os.system(f'gdal_translate -ot Byte -of PNG -b 1 -b 2 -b 3 -scale ./result2/ign/{file[:-4]}.jp2 ./final/ign/{y}.PNG')
    y+=1
    print()
print("done")

#Options de la commande gdal_translate :
# -ot Byte : Permet de régler la plage de valeur des pixels en sortie (Byte = 0 - 255)
# -of PNG : Permet de régler le format voulu en sortie (PNG = .PNG)
# -b 1 -b 2 -b 3 : Permet de ne garder que les 3 premières bandes (RGB) de l'image
# -scale : Permet de pouvoir réajuster les couleurs pour obtenir une image PLEIADES notamment de meilleur qualité