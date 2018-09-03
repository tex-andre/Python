num = int(input("Introduza um numero:"))

list_range = list(range(1, num + 1))

lista_divisores = []

for x in list_range:
    if num % x == 0:
        lista_divisores.append(x)

print(lista_divisores)
    