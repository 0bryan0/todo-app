import todo_functions as functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do.")
input_box = gui.InputText(tooltip="Enter todo.", key='todo')
add_button = gui.Button("Add")
remove_button = gui.Button("Remove")
edit_button = gui.Button("Edit")
list_box = gui.Listbox(values=functions.get_todos(), key='todos', 
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
remove_button = gui.Button("Remove")

window = gui.Window('To-Do App', 
                    layout=[[label], [input_box, add_button], 
                    [list_box, edit_button, remove_button]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case gui.WIN_CLOSED:
            break

        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            if new_todo == todo_to_edit:
                continue
            new_todo = new_todo + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Remove":
            todo_to_remove = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_remove)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        


window.close()