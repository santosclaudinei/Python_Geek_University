def quadrado_perfeito(numero):
    raiz = numero ** (1/2)
    if (raiz ** 2) == numero:
        print(f"O numero digitado foi {numero} e a raiz foi {raiz}. Portanto é um quadarado perfeito")
    else:
        print(f"O numero digitado foi {numero} e a raiz foi {raiz}. Portanto não é um quadarado perfeito")


num = int(input("Digite um numero: "))
quadrado_perfeito(num)