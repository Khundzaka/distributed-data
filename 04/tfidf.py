from Executor import Executor
from functools import reduce


def job1_mapper(file, data, emit):
    split_words = data.split(" ")
    result = []
    for word in split_words:
        temp = word.lower()
        temp = "".join([i for i in temp if i not in '.,?\'\\"'])
        result.append(temp)
    filtered_list = list(filter(lambda x: len(x) > 0, result))

    for word in filtered_list:
        emit((file, word), 1)

def job1_reducer(key, items, emit):
    result = reduce(lambda agg, x: agg+x, items, 0)
    emit(" ".join(key), result)

exec = Executor('input', job1_mapper, job1_reducer)

exec.execute_and_write(folder="output1")

def job2_mapper(file, data, emit):
    key, value = data.split("\t")
    filename, word = key.split(' ')
    print(filename, word)
    emit(filename, (word, value))

def job2_reducer(key, items, emit):
    result = reduce(lambda agg, x: agg+int(x[1]), items, 0)
    for item in items:
        emit(" ".join([item[0], key]), " ".join([item[1], str(result)]) )

exec = Executor('output1', job2_mapper, job2_reducer)

exec.execute_and_write(folder="output2")