valorHora = float(input("Informe o valor da hora trabalhada: "))
horasMes = float(input("Informe o numero de horas trabalhadas no mês: "))
salarioMes = valorHora * horasMes
print(f"O seu salario é {salarioMes} e com o bonus ficou {salarioMes + salarioMes * 0.10}")