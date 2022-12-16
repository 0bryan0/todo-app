
def get_todos(filepath):
    """ return a list of current todos into a file """

    with open(filepath, 'r') as file:
            todos = file.readlines()
    return todos

def write_todos(filepath, todos):
    """ write new set of todos into a file """
    with open(filepath, 'w') as file:
            file.writelines(todos)