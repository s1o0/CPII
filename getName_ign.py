from osgeo import ogr
#Objectif : Récupérer le nom de l'image IGN associée à une tuile
#Prérequis : Ogr, Python

#Méthode permettant de pouvoir récupérer le nom d'une image IGN en fonction d'un fichier .shp
def getName(shapefile):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    #On ouvre le fichier .shp
    ds = driver.Open(shapefile, 0)
    layer = ds.GetLayer()

    #On récupère les valeurs présentes dans les tables d'attributs
    for feature in layer:
        print (feature.GetField("NOM"))
        print (feature.GetField("ID"))
        x = feature.GetField("NOM")
    #On return la variable X comportant le nom de l'image IGN associée
    return x
        
if __name__=='__main__':
    s = getName('./test.shp')
    print()
    print(s)