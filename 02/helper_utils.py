from os import walk, path

def get_list_of_files(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        # print(dirpath, dirnames, filenames)
        f.extend(list(map(lambda x: path.join(dir,x), filenames)))
        break
    return f

def read_lines(filename):
    file = open(filename, 'r', encoding="utf-8")

    content = file.read()

    return content.split("\n")