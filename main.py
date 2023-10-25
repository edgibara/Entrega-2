#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:06:20 2023

@author: edgibara
"""


class Usuario:
    _forbidden:str =['ç',' ','.']
    _users={'Eduardo': 6978309196542779321,
             'Bob': 8541747932423710418,
             'root0':-2954852157039356282}
    _levels={'Eduardo': 'Visitor',
              'Bob':'Admin',
              'root0':'su'}
    def __init__(self,user: str,senha: str) -> None:
        try:
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
        if self.__name in self._users.keys():
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
    def get_name(self):
        return self.__name
    @property
    def get_level(self):
        return self.__acess
class Admin(Usuario):
    _usrscounter=3
    def new_usr(self,nam: str,pasw:str,level:int) -> None:
        if self.get_level <=level:
            print('Solicitacao Negada')
        else:    
            new={nam:pasw}
            self._users.update(new)
            print('Novo usuario adicionado')
            self._usrscounter+=1
class root(Admin):
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

    
