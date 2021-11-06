from Executor import Executor
from functools import reduce


def job1_mapper(file, data, emit, mem):
    cur, nodes = data.split("\t")

    distance = -1

    if cur == '0':
        distance = 0

    print((cur, nodes),)

    nodes = [i for i in nodes.split(" ") if len(i) > 0]

    emit(cur, [distance, nodes])
    if distance != -1:
        for node in nodes:
            emit(node, ['Distance',distance + 1])

def job1_reducer(key, items, emit, mem):
    min_distance = -1
    nodes = None
    print(items)

    for item in items:
        if item[0] != 'Distance':
            print(len(item))
            cur_distance, nodes = item
            if cur_distance != -1:
                if min_distance == -1:
                    min_distance = cur_distance
                else:
                    min_distance = min(cur_distance, min_distance)
                
        else:
            item = int(item[1])
            if min_distance == -1:
                min_distance = item
            else:
                min_distance = min(min_distance, item)
    
    infinity = 0 if min_distance >= 0 else 1
    if 'infinities' not in mem:
        mem['infinities'] = infinity
    else:
        mem['infinities'] += infinity

    emit(key, "{};{}".format(min_distance, " ".join(nodes)))

exec = Executor('input', job1_mapper, job1_reducer)

print(exec.execute_and_write('out1.txt', 'out1'))
print(exec.memory)