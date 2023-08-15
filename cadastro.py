from PySimpleGUI import PySimpleGUI as sg

#Layoyt
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(50,1))],
    [sg.Text('Senha '),sg.Input(key='senha',password_char='*',size=(50,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de Login', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if  valores['usuario'] == 'thiago' and valores ['senha'] == '123456':
            print('Bem vindo ao Sistema')
        