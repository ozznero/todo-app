import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            print(todos)
            new_todo = values['todo'] + "\n"
            print(new_todo)
            todos.append(new_todo)
            print(todos)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()
