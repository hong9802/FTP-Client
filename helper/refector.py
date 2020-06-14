def get_filename(path):
    if(path.find("/") == -1):
        return path
    else:
        paths = path.split("/")
        return paths[len(paths)-1]

def get_filepath(path):
    if(path.find("/") == -1):
        return ""
    else:
        paths = path.split("/")
        paths.pop(-1)
        return "/".join(paths) + "/"