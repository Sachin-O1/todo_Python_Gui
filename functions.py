FILEPATH = "todos.txt"

def _todos(todos_arg=None, filepath=FILEPATH):
    if todos_arg is None:
        with open(filepath, 'r') as file_local:
            return file_local.readlines()
    else:
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)


if __name__ == "__main__":
    _todos()