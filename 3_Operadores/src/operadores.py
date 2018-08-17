# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    remainder = 11 % 3 #resto da divisao
    print(remainder)
    
    squared = 7 ** 2 #potencias
    cubed = 2 ** 3
    print(squared)
    print(cubed)
    
    string = "Hello" + " " + "world" #somma de strings
    print(string) 
    string2 = " how are you today?"
    print("\n" + string + "," + string2)
    
    lotsofhellos = "hello " * 10 #multiplicacao de strings
    print(lotsofhellos) 
    
    even_numbers = [2,4,6,8]
    odd_numbers = [1,3,5,7]
    all_numbers = odd_numbers + even_numbers # soma de listas
    print(all_numbers)
    
    all_numbers.sort() # ordenar uma lista
    print(all_numbers) 
    
    print([1,2,3] * 3) # repeticao de uma string
    
    print(all_numbers * 2) #repeticao de uma lista