import os

def parse_name_file(name):
    l = name[:len(name)-4]
    return l    

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