num_alunos = int(input("Digite o número de Alunos: "))

dados_alunos = []
soma_media_turma = 0

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))

    #calcular média do aluno
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    #Adicionar os dados do aluno à lista
    dados_alunos.append((nome, nota1, nota2, nota3, media, status))

    #somar média turma.
    soma_media_turma += media

# Calcular a média geral da turma.
media_turma = soma_media_turma / num_alunos

print("\nResultados:")
for aluno in dados_alunos:
    nome, nota1, nota2, nota3, media, status = aluno
    print(f"\nNome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

print(f"\nMédia geral da turma: {media_turma:.2f}")