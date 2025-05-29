notas = []

while True:
    nota = float(input("Digite a nota do aluno -1 para sair: "))

    if nota == -1:
        break

    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Quantidade de alunos:", len(notas))
    print("Média da turma:", media)
else:
    print("Nenhuma nota foi digitada.")
print(f"media decimal {media:.2f}")