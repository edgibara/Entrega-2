#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:06:20 2023

@author: edgibara
"""

#%% Criar uma classe para controlde de usuario, tem
# nome de usuario, regras para o nome, se n obedecer as regras o nome n existe, ex: ele n pode ter espaço virgula ou alguns outros caracteres
# hash como password n vao guardar a password mas a hash dele
# rule -> 3 niveis no minimo de usuario
#metodos pra verificar senha:
#metodo para verificar atribuiçoes
#entrada nome de usuario/senha e retornar ok admin ok usuario normal ou nao ok nome n existe

class Usuario: #Objetos inicializados dessa classe sao usarios logados, variaveis privadas e protegidas foram usadas.
    _forbidden:str =['ç',' ','.']
    _users={'Eduardo': 6978309196542779321, #Dicionario com os nomes de usarios e hashs de suas senhas
             'Bob': 8541747932423710418,
             'root0':-2954852157039356282}
    _levels={'Eduardo': 'Visitor', #Dicionario com o nome de seus usuarios e seus niveis hierarquicos
              'Bob':'Admin',
              'root0':'su'}
    def __init__(self,user: str,senha: str) -> None: #Metodo de inicializacao do objeto
        try: #Codigo que tenta que inicializar um objeto e falha se tem algo de errado com o nome
            self.__name=user
            self.__pasw=hash(senha)
            for letter in user:
                if letter in self._forbidden:
                    raise Exception(ValueError)
        except ValueError:
            print("Caracter Proibido")
            del self.__name
            del self.__pasw
        except TypeError:
            print("Nome nao eh string")
            del self.__name
            del self.__pasw
        if self.__name in self._users.keys(): #Ifs que checam se o usario possui dados validos
            if self.__pasw == self._users[self.__name]:
                try:
                    match self._levels[self.__name]:
                        case 'Visitor':
                            print('Bem vindo usuario visitante')
                            self.__acess=0
                        case 'Admin':
                            print('Bem vindo usuario administrador')
                            self.__acess=1
                        case 'su':
                            print('Bem vindo super usuario ')
                            self.__acess=2
                except KeyError:
                    print("O usuario mencionado nao possui nivel registrado")
            else:
                print('Nome de usuario ou senha incorretos')
        else:
            print('Nome de usuario ou senha incorretos')
    @property
    def get_name(self): #Funcao getter do proprio nome do user
        return self.__name
    @property
    def get_level(self): #Funcao getter do nivel na hierarquia do usuario
        return self.__acess
class Admin(Usuario): #Subclasse de usuario com alguns privilegios, consegue ver quandos usuarios estao registrados e criar novos
    _usrscounter=3
    def new_usr(self,nam: str,pasw:str,level:int) -> None:
        if self.get_level <=level:
            print('Solicitacao Negada')
        else:    
            new={nam:pasw}
            self._users.update(new)
            print('Novo usuario adicionado')
            self._usrscounter+=1
class root(Admin): #Subclasse de Admin, possui todos os privilegios possiveis podendo criar novos caracteres proibidos
    def setforbidden(self,word:str)-> None:
        if len(word)==1:
            self._forbidden.append(word)
            print("Caracter:",word,"foi adicionado com sucesso")
        else:
            print("Erro, apenas um caracter pode ser adicionado a lista")
#Exemplo de usuario visitante entrando e checando seus dados:  
s=Usuario('Eduardo','senha')
print(s._Usuario__name)
print(s.get_name)
print(s.get_level)
#Exemplo de logins incorretas:
#s2=Usuario('Bob','ffdvd')
    # s3=Usuario('cd ..',' ')
#Exemplo de usuario admin criando novo visitante:
s4=Admin('Bob','314159') 
s4.new_usr('Lucas',hash('senha_de_Lucas'),0)
#Exemplo de usuario root checando seu nome e adicionando novo caracter proibido:
s5=root('root0','Changeme123')
print(s5.get_name)
s5.setforbidden('~')

    
