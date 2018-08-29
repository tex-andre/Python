class Pessoa():
    def __init__(self, nome, sobrenome, idade): # Executada na criacao de um objecto desta classe
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def nome_completo(self): #os metodos tem de receber self, as variaveis da classe
        return self.nome + " " + self.sobrenome
    
    def apresentacao(self):
        return "O meu nome e %s e tenho %d anos!" %(self.nome_completo(), self.idade)
    