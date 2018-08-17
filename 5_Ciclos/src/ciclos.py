# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    primes = [2, 3, 5, 7]
    #Exemplos de ciclos for
    for x in primes: # x: variavel iteradora 
        print(x)    
    print("\n")
    
    for x in primes:  
        print(primes) #imprime toda a lista
    print("\n")
    
    for x in range(3, 8, 2): #imprime os numeros de 3 a 8 (8 nao inclusive) de dois em dois 
        print(x)
        
    print("\n")
    # Exemplo de ciclo while e uso de else em ciclos:
    count = 0
    while count < 5:
        print(count)
        count += 1
    else:           # Quando a condicao do while nao se verificar, o codigo do else e executado
        print("O valor de count e: %d\n" % count)
    
    for i in range(1, 10):
        if (i % 5) == 0:
            break
        print(i) #imprime de 1  a  4
    else:
        print("Este codigo nao e executado por causa do break  e nao pela invalidade do ciclo for.")
    