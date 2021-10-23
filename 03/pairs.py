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
        for second in unique_words:
            emit((first, second), obj[second])
            emit((second, first), obj[first])

def reducer(key, items):
    return reduce(lambda agg, x: agg+x, items, 0)

exec = Executor('input', mapper, reducer)

result = exec.execute()

for pair in result:
    print(pair[0], " => ", pair[1])

# def aggregator_func(agg, s):
#     print (agg, s)
#     return agg + s

# result = reduce(aggregator_func, ['lorem', 'ipsum', 'it', 'sometimes'])

# print (result)