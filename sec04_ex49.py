hora = int(input("Informe a hora: "))
minuto = int(input("Informe o minuto: "))
segundo = int(input("Informe o segundo: "))
duracaoSegundos = int(input("Informe a duração do evento: "))
duracaoMinutos = duracaoSegundos / 60
duracaoHora = int(duracaoMinutos/60)
duracaoMinuto = int(duracaoMinutos / 60 - duracaoHora) * 60
print(f"{duracaoMinutos}\n\n")
print(f"{hora}\n"
      f"{minuto}\n"
      f"{segundo}\n"
      f"{duracaoHora}\n"
      f"{duracaoMinuto}")

