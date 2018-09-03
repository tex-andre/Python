'''
Created on 03/09/2018

@author: tex
'''

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.jogada = ""
        
    def Jogada(self, escolha):
        self.jogada = escolha
        