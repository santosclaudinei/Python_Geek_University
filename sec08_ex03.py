def verificar_numero(numero):
    if (numero > 0):
        return 1
    elif (numero < 0):
        return -1
    return 0


num = int(input("Digite um numero: "))
if (verificar_numero(num) == 1):
    print("O numero digitado é positivo.")
elif (verificar_numero(num) == -1):
    print("O numero digitado é negativo.")
else:
    print("numero digitado é zero.")