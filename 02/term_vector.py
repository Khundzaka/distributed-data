# to run this script, there are two options:
# 1 - run the script and make sure working directory is set to 02 folder
# 2 - run the script from terminal by going to folder 02 by command "cd 02" and then run by "python term_vector.py"
# If you have mac or linux, python version 3 command might be "python3" instead of "python"

from helper_utils import get_list_of_files, read_lines
from Executor import Executor


def mapper_function(filename, line, push):
    split_words = line.split(' ')
    result = []
    for word in split_words:
        result.append(word.lower())

    filtered_list = list(filter(lambda x: len(x) > 0, result))

    obj = {}

    for word in filtered_list:
        if word in obj:
            obj[word] += 1
        else:
            obj[word] = 1

    for el in obj.items():
        push(filename, el)

def reducer_function(key, results):
    mem = {}

    for word, freq in results:
        if word in mem:
            mem[word] += freq
        else:
            mem[word] = freq


    def key_selector(x):
        return x[1]
    
    most_frequent = list(sorted(mem.items(), key=key_selector, reverse=True))[0]

    return most_frequent

executor = Executor('input', mapper_function, reducer_function)

print(executor.execute())
