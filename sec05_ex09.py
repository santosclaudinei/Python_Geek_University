salario = float(input("Informe o salario do trabalhador: "))
valorPrestacao = float(input("Informe o valor da parcela: "))

if (valorPrestacao > (salario * 0.20)):
    print("Emprestimo não concedido.")
else:
    print("Emprestimo concedido.")