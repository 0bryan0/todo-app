import todo_functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do.")
input_box = gui.InputText(tooltip="Enter a todo.")

window = gui.Window('To-Do App', layout=[[label, input_box]])
window.read()
window.close()