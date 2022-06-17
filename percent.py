import cv2

def percent_black(file):
    img = cv2.imread(file,-1)
    lst = []
    lst.append(img.shape)
    #print(lst)
    #print(lst[0][0])
    #rows, cols= img.shape

    noirs = 0 
    pixels = 0
    
    i=0 
    while i < lst[0][0]:
        j=0
        while j<lst[0][1]:
            k = img[i,j]
            if str(k) == "[0. 0. 0. 0.]" or str(k)=="0.0" or str(k)=="0" or str(k)=="0.":
                noirs +=1 
            pixels +=5 
            j+=5
        i+=5
    x = (noirs*100/pixels)*5
    print(noirs*100/pixels)
    return x

'''if __name__=='__main__':
    a=percent_black('./result/5/1/OUTPUT.tif')'''
    
