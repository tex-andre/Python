if __name__ == "__main__":
    from Classe_pessoa import Pessoa
    
    nome = input("Nome: ")
    sobrenome = input("Sobreome: ")
    idade = int(input("Idade: "))
    
    andre = Pessoa(nome, sobrenome, idade) # cria um novo objecto da classe Pessoa
    
    print (andre.apresentacao())
    
    #del andre.sobrenome       -> apaga a variavel sobrenome do objecto
    #del andre                 -> apaga o objecto