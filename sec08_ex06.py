def converter_em_segundos(hour, minute, second):
    cont_segundos = (int(hour) * 3600) + (int(minute) * 60 ) + int(second)
    return (cont_segundos)


h = input("digite a hora desejada: ")
hora, minuto, segundo = h.split(":")
print(f"A conversão da quantidade de horas, minutos e segundos em segundos é: "
      f"{converter_em_segundos(hora, minuto, segundo)}")