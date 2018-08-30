if __name__ == "__main__":
    import os #importa  biblioteca "os" para poder manipular ficheiros
    
    ficheiro = "teste.txt"
    
    fp = open(ficheiro, "wt")
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