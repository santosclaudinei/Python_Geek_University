from math import log

num = int(input("Informe um numero: "))

if num < 0:
    print("Numero invalido.")
else:
    print(f"{log(num)}")
