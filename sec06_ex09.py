cont = 1
numero = int(input("Informe um numero: "))
while cont < numero * 2 + 1:
    if cont % 2 != 0:
        print(cont)
    cont += 1