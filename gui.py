import todo_functions as functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do.")
input_box = gui.InputText(tooltip="Enter todo.", key='todo')
add_button = gui.Button("Add")
remove_button = gui.Button("Remove")
edit_button = gui.Button("Edit")

window = gui.Window('To-Do App', 
                    layout=[[label], [input_box, add_button]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        case sg.WIN_CLOSED:
            break
        
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)


window.close()