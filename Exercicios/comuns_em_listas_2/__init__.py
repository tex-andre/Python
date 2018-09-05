import random

def lista_aleatria(tam, num_min, num_max):
    return random.sample(range(num_min,num_max), tam)

def main():
    a = lista_aleatria(10, 0, 30)
    b = lista_aleatria(20, 5, 35)
    
    com = [x for x in a if x in b] #list comprehension
    
    print(a)
    print(b)
    print(com)

if __name__ == "__main__":
    main()