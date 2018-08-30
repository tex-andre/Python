ficheiro = "teste.txt"

fw = open(ficheiro, "wt") #cria uma variavel fw para aceder ao ficheiro para escrita de texto ("wt")
fw.write("Hello world!\n" * 5)

fw.close() # Antes de ler o ficheiro e necessario usar close()

fr = open(ficheiro, "rt")

for x in fr:
    print(x)

fr.close()