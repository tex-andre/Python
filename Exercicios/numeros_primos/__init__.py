def num_primo(num):
    if num == 0:
        exit()
    for x in range(2, num):
        if num % x  == 0:
            return 0
    return 1

def escreve_resultado(num):
    if num_primo(num):
        x = ""
    else:
        x = " nao"
    print("Este numero%s e um numero primo." % x)
        
def pede_num():
    num = int(input("Introduza um numero: "))
    return num

escreve_resultado(pede_num())