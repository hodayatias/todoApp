FILEPATH='todo.txt'

def get_todos(filepath=FILEPATH):
    with (open(filepath, 'r') as file):
        new_todos = file.readlines()
    return new_todos


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)