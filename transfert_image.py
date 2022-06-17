from osgeo import gdal
import os
from parse_folder import parse_folder

x = open('./x.txt','r')
i = 1 
for lines in x:
    line = lines.strip()
    os.system(f'gdal_translate -of GTiff -co COMPRESS=NONE -co BIGTIFF=IF_NEEDED {line} ./Img_Dim/{i}.tif')
    os.system(f'gdal_translate -a_srs EPSG:2154 -ot UInt16 -of GTiff ./Img_Dim/{i}.tif ./Images_reproj/{i}.tif')
    i+=1 
print("done")
	

