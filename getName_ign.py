from osgeo import ogr
def getName(shapefile):
    #shapefile = './1.shp'
    driver = ogr.GetDriverByName("ESRI Shapefile")
    ds = driver.Open(shapefile, 0)
    layer = ds.GetLayer()

    for feature in layer:
        print (feature.GetField("NOM"))
        print (feature.GetField("ID"))
        x = feature.GetField("NOM")
    return x
        
if __name__=='__main__':
    s = getName('./test.shp')
    print()
    print(s)