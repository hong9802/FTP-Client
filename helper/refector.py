import ntpath

def get_filename(path):
    return ntpath.basename(path)

def get_filepath(path):
    head, tail = ntpath.split(path)
    return head + "/"