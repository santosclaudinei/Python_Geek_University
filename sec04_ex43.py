valorCompra = float(input("Informe o valor da venda: "))

aVista = valorCompra - (valorCompra * 0.10)
aPrazo = valorCompra / 3
comissaoVista = (valorCompra * 0.10) * 0.05
comissaoPrazo = valorCompra * 0.05
print(f"O valor da compra foi {valorCompra}\n"
      f"pagando a vista fica {aVista}\n"
      f"Pagando em 3x fica {aPrazo:.2f}\n"
      f"Comissão do vendedor caso seja a vista será {comissaoVista}\n"
      f"Comissão do vendedor caso seja em 3x será {comissaoPrazo}\n")
