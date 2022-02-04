from json import dump, load

class Lista_clientes:
    '''Classe referente à listagem dos clientes'''
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.json_file = self.json_dict(self.arquivo)
    

    @staticmethod
    def json_dict(arquivo):
        '''Converte json em dicionário'''
        with open(arquivo, mode='r', encoding='UTF-8') as arquivo:
            dictionary = load(arquivo)
        return dictionary


    def adiciona_cliente(self, cliente):
        '''Função que adiciona os clientes à listagem'''
        self.json_file['clientes'].append(cliente.__dict__)
    

    def salva_dados(self):
        '''Converte o dicionário em json'''
        with open(self.arquivo, mode='w', encoding='UTF-8') as arquivo:
            dump(self.json_file, arquivo, indent=4)
    

    def leitura_arquivo(self):
        '''Função que faz a leitura do json e retorna uma lista com seus valores'''
        lista = list()
        for cliente in self.json_file['clientes']:
            lista.append(list(cliente.values()))
        return lista

    '''Módulo referente à listagem dos clientes'''
