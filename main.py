import PySimpleGui as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Texte('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login', Layout=layout)

while True:
    event, values = window.read
    if event == sg.WIN_CLOSED:
        break