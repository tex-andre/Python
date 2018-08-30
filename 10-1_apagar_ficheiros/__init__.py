if __name__ == "__main__":
    import os #importa  biblioteca "os" para poder manipular ficheiros
    
    ficheiro = "teste.txt"
    
    fp = open(ficheiro, "wt") #escrita de texto
    fp.write("Ola mundo!\nEu existo!") #escreve
    fp.close()
    
    if(os.path.exists(ficheiro)):   #verifica  se o ficheiro existe
        print("Sim, este ficheiro existe!\n")
        os.remove(ficheiro) #remove ficheiro na directoria
    
    if(os.path.exists(ficheiro)):
        print("Ainda existe!\n")
    else:
        print("Agora ja nao!\n")
        
    #Proximo: criar nova pasta e apagar
    
    novaDir = "teste" # nova pasta "teste"
    
    if(not os.path.exists(novaDir)): # se nao existe a pasta
        os.makedirs(novaDir) #cria
        print("Pasta criada!\n")
    else:       #se nao
        os.removedirs(novaDir) #apaga
        print("Pasta apagada!\n")