from Executor import Executor
from functools import reduce


def mapper(file, data, emit):
    split_words = data.split(" ")
    result = []
    for word in split_words:
        temp = word.lower()
        temp = "".join([i for i in temp if i not in '.,?\'\\"'])
        result.append(temp)
    filtered_list = list(filter(lambda x: len(x) > 0, result))

    obj = {}

    for word in filtered_list:
        if word in obj:
            obj[word] += 1
        else:
            obj[word] = 1

    unique_words = obj.keys()

    for first in unique_words:
        temp = {}
        for second in unique_words:
            temp[second] = obj[second]
        emit(first, temp)

def reducer(key, items):

    def reducer_func(agg, x):
        for item in items:
            for word in item.keys():
                agg[word] = agg.get(word, 0) + item[word]
        return agg

    return reduce(reducer_func, items)

exec = Executor('input', mapper, reducer)

result = exec.execute()

for pair in result:
    print(pair[0], " => ", pair[1])