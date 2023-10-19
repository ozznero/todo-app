import PySimpleGUI as sg
from zip_extr_backend import extract_archive

sg.theme("LightBlue")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",  key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window(title="Zip Extractor",
                   layout=[[label1, input1, choose_button1],
                    [label2, input2, choose_button2],
                    [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archive_path, dest_dir)
    window["output"].update(value="Extraction completed")
window.close()
