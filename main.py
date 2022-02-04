import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from Cliente import *
from Lista_clientes import *


def janela_inicial():
    '''Retorna a janela inicial com o layout descrito'''
    layout = [
                [sg.Text('Nome:', justification='left'), sg.Input(key='nome')],
                [sg.Text('Número:', justification='left'), sg.Input(key='numero')], 
                [sg.Text('Email:', justification='left'), sg.Input(key='email')], 
                [sg.Text('CPF:', justification='left'), sg.Input(key='cpf')], 
                [sg.Button('Enviar'), sg.Button('Sair'), sg.Button('Ver clientes')]
            ]
            
    return sg.Window(layout=layout, title='cadastro')


def janela_dados(dados):
    '''Retorna uma tabela com a listagem de clientes'''
    headers = ['Nome', 'Número', 'Email', 'CPF']
    layout = [
        [sg.Table(headings=headers, values=dados, justification='center', size=(80, len(dados)), auto_size_columns=True)],
        [sg.Button('Sair')]
    ]

    return sg.Window(layout=layout, title='clientes')


lista_clientes = Lista_clientes('arquivo.json')


def main():
    '''Função principal do sistema'''
    window = janela_inicial()

    while True:
        event, values = window.read()

        if event == 'Sair' or event == WINDOW_CLOSED:
            break

        elif event == 'Enviar':
            try:
                cliente = Cliente(values['nome'], values['numero'], values['email'], values['cpf'])
            except Exception as ERROR:
                sg.popup(ERROR)
            else:
                lista_clientes.adiciona_cliente(cliente)
                lista_clientes.salva_dados()
                sg.popup('Cliente salvo!')
                
        elif event == 'Ver clientes':
            window2 = janela_dados(lista_clientes.leitura_arquivo())

            while True:
                eve, val = window2.read()

                if eve == 'Sair' or eve == WINDOW_CLOSED:
                    break

            window2.close()

    window.close()

if __name__ == '__main__':
    main()
