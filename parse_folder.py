import os
#Objectif : Parser un fichier pour récupérer tous les noms des fichiers sans doublons
#Prérequis : Python

#Méthode permettante de pouvoir récupérer le nom d'un fichier sans son extension
def parse_name_file(name):
    l = name[:len(name)-4]
    return l    

#Méthode retournante un tableau comportant tous les noms des fichiers sans doublons
def parse_folder(path_to_folder):
    onlyfiles = os.listdir(path_to_folder)
    names=[]
    for files in onlyfiles:
        name = parse_name_file(files)
        if name not in names:
            names.append(name)
        else:
            pass
    return names