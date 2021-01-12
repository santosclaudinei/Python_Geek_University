num1 = int(input("Informe um numero: "))
num2 = int(input("Informe um numero: "))

if num1 > num2:
    print(f"O maior numero entre {num1} e {num2} é {num1}\n"
          f"A difernça entre eles é {num1 - num2}")
else:
    print(f"O maior numero entre {num1} e {num2} é {num2}\n"
          f"A difernça entre eles é {num2 - num1}")