from Classe_jogador import Jogador
import sys

def intro():
    print("Jogo pedra papel ou tesoura!\n")
    
def novo_jogador():
    nome = input("Nome: ")
    jogador = Jogador(nome)
    return jogador

def parabens(jogador):
    print("Parabens %s!" % jogador.nome)

def jogo(jogador1, jogador2):
    fim_de_jogo = 0
    while not fim_de_jogo:
        print("Vez do jogador 1:\n")
        jogador1.Jogada(input("Introduza a sua escolha: "))
        print("Vez do jogador 2:\n")
        jogador2.Jogada(input("Introduza a sua escolha: "))
        
        if vencedor(jogador1, jogador2) == 1:
            parabens(jogador1)
            fim_de_jogo = 1
        elif vencedor(jogador1, jogador2) == 2:
            parabens(jogador2)
            fim_de_jogo = 1
        else:
            print("Empate!\n")
    
    
def vencedor(jogador1, jogador2):
    if jogador1.jogada == "pedra":
        if jogador2.jogada == "tesoura":
            return 1
        elif jogador2.jogada == "papel":
            return 2
        else:
            return 0
    elif jogador1.jogada == "tesoura":
        if jogador2.jogada == "papel":
            return 1
        elif jogador2.jogada == "pedra":
            return 2
        else:
            return 0
    elif jogador1.jogada == "papel":
        if jogador2.jogada == "pedra":
            return 1
        elif jogador2.jogada == "tesoura":
            return 2
        else:
            return 0
    else:
        print("ERRO: opcao invalida!\n")
        sys.exit(1)
    
def outro():
    return int(input("Outro jogo?\n1 se SIM, 0 se NAO: "))

if __name__ == "__main__":
    intro()
    print("Jogador 1:\n")
    jogador1 = novo_jogador()
    print("Jogador 2:\n")
    jogador2 = novo_jogador()
    
    jogo(jogador1, jogador2)
    while outro():
        jogo(jogador1, jogador2)
    else:
        exit(0)