notas = []

for i in range(1,4):
    nota = float(input(f"informe a {i}ª nota: "))
    notas.append(nota)

nota1, nota2, nota3 = notas
media = ((nota1 + nota2) + nota3 * 2) / 4

if media > 6.0:
    print("Aluno Aprovado.")
else:
    print("Aluno Reprovado.")