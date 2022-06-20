import cv2
#Objectif : Algorithme permettant de calculer le % de nodata présent sur une image. L'algorithme parcourt 1 ligne / 5 et 1 colonne /5 pour gagner en rapidité.
#Prérequis : Opencv, Python.

def percent_black(file):
    #Ouverture de l'image avec la librairie opencv
    img = cv2.imread(file,-1)
    lst = []
    lst.append(img.shape)

    noirs = 0 
    pixels = 0
    
    i=0 
    #L'algorithme va boucler sur les pixels de l'image
    while i < lst[0][0]:
        j=0
        while j<lst[0][1]:
            k = img[i,j]
            #Si le pixels possède une de ces valeurs (qui correspondent à du nodata), alors on incrémente la variable "noirs"
            if str(k) == "[0. 0. 0. 0.]" or str(k)=="0.0" or str(k)=="0" or str(k)=="0.":
                noirs +=1 
            pixels +=5 
            j+=5
        i+=5
    #On réalise un produit en croix pour calculer le pourcentage
    x = (noirs*100/pixels)*5
    print(noirs*100/pixels)
    return x

'''if __name__=='__main__':
    a=percent_black('./result/5/1/OUTPUT.tif')'''
    
