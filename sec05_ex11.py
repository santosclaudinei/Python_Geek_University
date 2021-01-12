num = int(input("Informe um numero: "))
conv = str(num)

if num > 0:
    print(f"A soma dos digitos é {int(conv[0]) + int(conv[1]) + int(conv[2])}")
else:
    print("Numero invalido.")