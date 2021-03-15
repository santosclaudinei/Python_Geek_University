hora_chegada, minuto_chegada = input('Informe a hora de chegada: ').split()
hora_partida, minuto_partida = input('Informe a hora de partida: ').split()
hora_chegada = int(hora_chegada)
minuto_chegada = int(minuto_chegada)
hora_partida = int(hora_partida)
minuto_partida = int(minuto_partida)

duracao_hora = hora_partida - hora_chegada
duracao_min = minuto_partida - minuto_chegada

if hora_chegada == hora_partida and duracao_min < 1:
    duracao_hora = 24
elif hora_chegada > hora_partida:
    duracao_hora = 24 + duracao_hora
elif hora_chegada < hora_partida:
    duracao_hora = duracao_hora
if minuto_chegada == minuto_partida:
    duracao_min = 0
elif minuto_chegada > minuto_partida:
    duracao_min = 60 + duracao_min
    duracao_hora = duracao_hora - 1
elif minuto_chegada < minuto_partida:
    duracao_min = duracao_min

if duracao_min > 0:
    duracao_hora += 1
if 1 <= duracao_hora <= 2:
    tarifa = duracao_hora * 1.00
elif 3 <= duracao_hora <= 4:
    tarifa = duracao_hora * 1.40
else:
    tarifa = duracao_hora * 2.00

print(f'A duração foi {duracao_hora} e a tarifa a pagar é {tarifa:.2f}')


