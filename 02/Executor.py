from helper_utils import get_list_of_files, read_lines

class Executor:
    def __init__(self, folder, mapper_function, reducer_function) -> None:
        self.mapper_result = {}
        self.folder = folder
        self.mapper_function = mapper_function
        self.reducer_function = reducer_function

    def execute_mapper(self, filename, line, push):
        return self.mapper_function(filename, line, push)

    def execute_reducer(self, key, result):
        return self.reducer_function(key, result)

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
        for key in self.mapper_result:
            result = self.execute_reducer(key, self.mapper_result[key])
            final_results.append((key, result))

        return final_results
