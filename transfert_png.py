import os 

x = os.listdir('./result2/pleiadec/')
y = 93
for file in x:
    os.system(f'gdal_translate -ot Byte -of PNG -b 1 -b 2 -b 3 -scale ./result2/pleiadec/{file} ./final/pleiade/{y}.PNG')
    os.system(f'gdal_translate -ot Byte -of PNG -b 1 -b 2 -b 3 -scale ./result2/ign/{file[:-4]}.jp2 ./final/ign/{y}.PNG')
    y+=1
    print()
print("done")