ficheiro = "teste.txt"

fw = open(ficheiro, "wt") #cria uma variavel fw para aceder ao ficheiro para escrita de texto ("wt")
fw.write("Hello world!")

fw.close() # Antes de ler o ficheiro e necessario usar close()

fr = open(ficheiro, "rt")
print(fr.read())

fr.close()