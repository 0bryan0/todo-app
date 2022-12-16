from todo_functions import get_todos, write_todos
import time

date = time.strftime("%b %d, %Y %H:%M:%S") 
print("It is ", now)

while True:
    user_input = input("Enter add, remove, edit, show, or exit: ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input.replace('add', "").strip()

        if len(todo) == 0:
            todo = input("Enter a todo: ") + '\n'
        
        todos = get_todos("todos.txt")
        todos.append(todo + '\n')

        write_todos('todos.txt', todos)

    elif user_input.startswith('remove'):
        try:
            remove_location_str = user_input.replace('remove', "").strip()
            if len(remove_location_str) == 0:
                remove_location_str = input("Enter location that you want to delete: ")
            remove_location = int(remove_location_str.strip())

            todos = get_todos("todos.txt")

            todos.pop(remove_location)
            write_todos('todos.txt', todos)

        except IndexError:
            print("Location does not exit.")
            continue

    elif user_input == 'show':
        todos = get_todos("todos.txt")
        for todo in todos:
            todo.strip(todo)
            print(f'{todos.index(todo)} - {todo}')

    elif user_input.startswith('edit'):
        try:
            edit_location_str = user_input.replace('edit', "").strip()
            if len(edit_location_str) == 0:
                edit_location_str = input("Enter location that you want edit: ")
            edit_location = int(edit_location_str.strip())

            todos = get_todos("todos.txt")

            edited_todo = input("Enter a new todo: ")
            todos[edit_location] = edited_todo + '\n'
        except ValueError:
            print("Your command is not valid. Please try again.")
            continue 

        write_todos('todos.txt', todos)

    elif user_input == 'exit':
        break


print("bye!")
