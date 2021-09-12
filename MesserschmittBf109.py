from attack import attack
import PySimpleGUI as sg
 
sg.theme('Black')   # Add a touch of color 
# All the stuff inside your window.
layout = [  [sg.Image('plane.png')],
            [sg.Text('URL'), sg.InputText()],
            [sg.Text('Threads'), sg.InputText()],
            [sg.Button('Attack'), sg.Button('Cancel')]   ]

# Create the Window
window = sg.Window('Messerschmitt Bf 109', layout, element_justification='c')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Attack':
        attack(int(values[2]), values[1])

window.close()