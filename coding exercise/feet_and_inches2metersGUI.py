import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(tooltip="enter the feet quantity",  key='feet')

inches_label = sg.Text("Enter inches")
inches_input = sg.Input(tooltip="enter the inches quantity", key='inches')

button = sg.Button("Convert")
exit_button = sg.Button("Exit")

meters_label = sg.Text(key='meters')

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [button, exit_button, meters_label]])

while True:
    try:
        event, values = window.read()
        meters = convert(values['feet'], values['inches'])
        meters_string = f"{meters} m"
        window['meters'].update(value=meters_string)
        match event:
            case "Exit":
                break
            case sg.WIN_CLOSED:
                break
    except ValueError:
        sg.Popup("Please provide two numbers")
window.close()