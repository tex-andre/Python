class Estudante : #classe
    
    #variaveis da classe
    primeiro_nome = "Andre"
    ultimo_nome =  "Teixeira"
    numero = 20577
    
    def nome_completo(self):
        return self.primeiro_nome + " " + self.ultimo_nome
    
    #Metodo
    def apresentacao(self): #recebe self para aceder a variaveis da classe
        return "O meu nome e %s e sou o numero %d" %(self.nome_completo(), self.numero)
    