#cria dicionario
meu_dic = {}

#atribui elementos
meu_dic["nome"] = "Andre"
meu_dic["numero"] = 20577
meu_dic["idade"] = 25

#imprime todo o dicionario
print(meu_dic)

#imprime o valor para a chave ou index "nome"
print (meu_dic["nome"])

#altera nome
meu_dic["nome"] = "Andre Teixeira"

#apaga item
del meu_dic["idade"]

print(meu_dic)

#iteracao
#
# como em php, foreach $key => $value
for key, value in meu_dic.items(): 
    print(key, "=>" , value)
    