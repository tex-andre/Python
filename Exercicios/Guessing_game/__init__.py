import random

def intro ():
    print("Este codigo ira gerar um numero aleatorio que tera de adivinhar.\n")

def gera_num(num_min, num_max): 
    return random.randint(num_min, num_max)

def jogo():
    vezes = 0
    numero = gera_num(0,100)
    while 1:
        escolha = input("Escolha um numero: ")
        if escolha.isdigit():
            escolha = int(escolha)
            vezes += 1
            if escolha == numero:
                print("Parabens, acertou!\n")
                print("Numero de tentativas: %d\n" %vezes)
                break
            elif escolha > numero:
                print("%d e maior do que o numero gerado, tente outra vez!\n" % escolha)
            elif escolha < numero:
                print("%d e menor do que o numero gerado, tente outra vez!\n" % escolha)
        elif escolha == "exit":
            break
        else:
            print("Opcao invalida!\n")
            continue
    
if __name__ == "__main__":
    intro() 
    jogo()
        