from re import findall 
from validate_docbr import CPF 


class Cliente:
    '''Classe referente ao cadastro do cliente'''
    def __init__(self, nome, numero, email, cpf):
        self.__nome = self.formata_nome(nome)
        self.__numero = self.valida_numero(numero)
        self.__email = self.valida_email(email)
        self.__cpf = self.valida_cpf(cpf)
    

    @staticmethod
    def formata_nome(nome):
        '''Retorna o nome do usuário com as iniciais em maiúsculo'''
        if nome == '':
            raise ValueError('Digite seu nome!')
        return str(nome).strip().title()
        
    
    @staticmethod
    def valida_numero(numero):
        '''Valida o numero telefônico do usuário'''
        if numero == '':
            raise ValueError('Digite seu número!')
        numero = str(numero).strip()
        for num in numero:
            if num == '(' or num == ')' or num == '-' or num == ' ':
                numero = numero.replace(num, '')
        if len(numero) != 11:
            raise ValueError('Número inválido!')
        else:
            model_numero = ('[0-9]{2}9[0-9]{8}')

            if findall(model_numero, numero):
                return f'({numero[0:2]}) {numero[2:7]}-{numero[7:]}'
            else:
                raise ValueError('Número inválido!')
    

    @staticmethod
    def valida_email(email):
        '''Valida o email do usuário'''
        if email == '':
            raise ValueError('Digite seu email!')
        email = str(email).strip()
        model_email = ('^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$')
        if findall(model_email, email):
            return email
        else:
            raise ValueError('Email inválido!')
    

    @staticmethod
    def valida_cpf(cpf):
        '''Valida o CPF do usuário'''
        if cpf == '':
            raise ValueError('Digite seu cpf!')
        for caractere in cpf:
            if caractere == '.' or caractere == '-':
                cpf = cpf.replace(caractere, '')
        cpf = str(cpf).strip()
        valida = CPF()
        if valida.validate(cpf):
            return valida.mask(cpf)
        else:
            raise ValueError('CPF inválido')

'''Módulo responsável pela definição e validação das informações o cliente'''