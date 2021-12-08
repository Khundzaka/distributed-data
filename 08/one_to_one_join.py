from Executor import Executor

def mapper_func(filename, data, emit, mem):
    if 'Store' in data:
        return
    values = data.split(',')
    store = int(values[0])
    value = values[1]
    value_type = 'S' if 'stores' in filename else 'T'
    print(store, value_type, value)
    emit(store, (value_type, value))

def reducer_func(key, items, emit, mem):
    print (key, items)
    temp = ''
    type = ''
    for item in items:
        if item[0] == 'S':
            type = item[1]
        if item[0] == 'T':
            temp = item[1]
    if type == 'A' and int(temp or 0) >= 22:
        emit(key, ','.join([type, temp]))

e = Executor('input01', mapper_func, reducer_func)

print(e.execute())