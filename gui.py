import todo_functions as functions
import PySimpleGUI as gui
import time

gui.theme('DarkTeal12')

clock = gui.Text('', key='clock')
label = gui.Text("Type in a to-do.")
input_box = gui.InputText(tooltip="Enter todo.", key='todo')
add_button = gui.Button("Add")
remove_button = gui.Button("Remove")
edit_button = gui.Button("Edit")
list_box = gui.Listbox(values=functions.get_todos(), key='todos', 
                       enable_events=True, size=[45,12])
edit_button = gui.Button("Edit")
remove_button = gui.Button("Remove")
exit_button = gui.Button("Exit")


window = gui.Window('To-Do App', 
                    layout=[[clock], 
                            [label], [input_box, add_button], 
                            [list_box, edit_button, remove_button], 
                            [exit_button]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
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
            try:
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
            except IndexError:
                gui.popup("Please select a task to edit.", font=("Helvetica", 20))

        case "Remove":
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                gui.popup("Please select a task to edit.", font=("Helvetica", 20))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        


window.close()