def polindorme(str1):
    inv = str1[::-1] #inverte string
    if inv == str1:
        return 1
    else:
        return 0
str1 = str(input("Introduza uma string: "))
print(polindorme(str1))