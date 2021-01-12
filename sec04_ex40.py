numDias = int(input("Informe a quantidade de dias trabalhados: "))
valorDia = 30
salario = valorDia * numDias
print(f"O encanador trabalhou {numDias} ao valor de R$ {valorDia} "
      f"portanto seu salario é R$ {salario - salario * 0.08}")