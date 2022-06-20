# CPII
Algorithme permettant de découper les images Pleiades en fonction des images IGN

# Exécution :

Exécuter cette commande dans un terminal :
```bash
python3 transfert_image.py
```
Puis :
```bash
python3 main.py
```

# Description :
• getName_ign.py : Script permettant de récupérer le nom d'une image IGN en fonction de sa tuile

• main.py : Script "moteur" de l'algorithme, c'est ce script qu'il va réaliser les découpes. Les résultats se trouveront dans le dossier "result2"

• parse_folder.py : Script permettant de parser les dossiers

• percent.py : Script permettant de calculer le % de nodata (= pixels noirs) sur les images

• transfert_image.py : Script permettant de générer des images PLEIADES en fonction d'un fichier DIM

• transfert_png.py : Script permettant de transformer les images produites au format PNG. Les résultats se trouveront dans le dossier "final"

# Documentation nécessaires :
Une documentation a été réalisé via le logiciel Notion, vous pouvez la trouver sur ce [document](https://resonant-tamarillo-324.notion.site/Github-D-coupe-des-PLEIADES-e7c4b663c63b4067adb4a7bd9aa5f586).
