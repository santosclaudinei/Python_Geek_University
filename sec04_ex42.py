salario = float(input("Informe o salario do funcionario: "))
gratificacao = 5 / 100
inss = 7 / 100
print(f"O salario do funcionario é {salario} com bonus de {gratificacao} e desconto do INSS de {inss} resultando "
      f"num salario liquido de {salario + (salario * gratificacao) - (salario * inss)}")