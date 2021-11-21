from os import walk, path, makedirs

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


class Executor:
    def __init__(self, folder, mapper_function, reducer_function) -> None:
        self.mapper_result = {}
        self.folder = folder
        self.mapper_function = mapper_function
        self.reducer_function = reducer_function
        self.memory = {}

    def execute_mapper(self, filename, line, emit):
        return self.mapper_function(filename, line, emit, self.memory)

    def execute_reducer(self, key, result, emit):
        return self.reducer_function(key, result, emit, self.memory)

    def execute(self):
        files = get_list_of_files(self.folder)

        def append_to_mapper(key, value):
            if key in self.mapper_result:
                    self.mapper_result[key].append(value)
            else:
                self.mapper_result[key] = [value]

        for file in files:
            lines = read_lines(file)

            # mapper stage
            for line in lines:
                self.execute_mapper(file, line, append_to_mapper)

        final_results = []
        # reducer stage
        def append_to_reducer(key, value):
            final_results.append((key, value))

        for key in self.mapper_result:
            self.execute_reducer(key, self.mapper_result[key], append_to_reducer)
        final_results.sort(key=lambda x: x[0])
        return final_results

    def execute_and_write(self, filename='default.txt', folder="output"):
        if not path.exists(folder):
            makedirs(folder)
        result = self.execute()
        mapped_result = map(lambda x: "{}\t{}".format(x[0], x[1]), result)
        final_result = "\n".join(mapped_result)
        f = open(path.join(folder, filename), 'w', encoding='utf-8')
        f.write(final_result)