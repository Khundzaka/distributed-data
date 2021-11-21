from Executor import Executor

def mapper_func(file, data, emit, mem):
    if 'Fuel_Price' in data:
        return
    values = data.split(',')
    year = values[1].split('/')[-1]
    fuel_price = float(values[3])

    emit(year, fuel_price)

def reducer_func(key, items, emit, mem):
    average = sum(items) / len(items)
    emit(key, str(average))

e = Executor('input', mapper_func, reducer_func)

e.execute_and_write()