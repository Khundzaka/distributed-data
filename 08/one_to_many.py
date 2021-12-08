from Executor import Executor

def mapper_func(filename, data, emit, mem):
    if 'Store' in data:
        return
    values = data.split(',')
    store = int(values[0])
    table = 'S' if 'stores' in filename else 'F'
    value = values[1] if table == 'S' else values[2]
    emit(store, (table, value))

def reducer_func(key, items, emit, mem):
    # print(key, items)
    type = ''
    for item in items:
        if item[0] == 'S':
            type = item[1]
            break
    if type == 'A':
        for item in items:
            if item[0] == 'F':
                emit(key, ','.join([type, item[1]]))

e = Executor('input02', mapper_func, reducer_func)

print(e.execute())