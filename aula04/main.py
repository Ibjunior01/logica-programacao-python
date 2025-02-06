'''
O loop for itera sobre uma função (lista, tupla, string ou range)

palavra = "python"
for letra in palavra:
    print(letra)

for i in range(1, 10, 2): #1 stant / 10 stop/ 2 step(passo)
    print(i)


#Atividade 01
numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')


#Atividade 02
soma = 0
for i in range(1, 101):
    soma += i
print(f"A soma total dos números de 1 a 100 é: {soma}")
# OBSERVAÇÃO: O print identado com o for imprime a soma 100x. 


#Atividade 03
palavra = input("Digite uma palavra: ")
for letra in palavra:
    print(letra)


#Atividade 04
for i in range(10, 0, -1):
    print(i)
print("feliz ano novo!")


# FOR + CONDICIONAIS (if, elif, else):
for i in range (1, 11):
    if i % 2 == 0: #imprime apenas os números pares. 
        print(f"{i} é par")

        
texto = "Programação em Python"
contador_vogais = 0
for caractere in texto:
    if caractere.lower() in "aeiou":
        contador_vogais += 1
print(f"Número de vogais: {contador_vogais}")


#Atividade 05
positivos = 0
negativos = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")

#Atividade 06
soma_pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma_pares += i
print(f"A soma total dos números pares de 1 a 50 é: {soma_pares}")


#Atividade 07
palavra = input("Digite uma palavra: ")
contagem_vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        contagem_vogais += 1
print(f"A palavra {palavra} contém {contagem_vogais} vogais")


#Atividade 08
soma_notas = 0 
for i in range(5):
    nota = float(input("Digite a nota {i+1}: "))
    soma_notas += nota

media = soma_notas / 5
if media >= 6:
    classificacao = "Aprovado"
else:
    classificacao = "Reprovado"

print(f"A média das notas é: {media:.2f}")
print(f"Classificação: {classificacao}")


#Combinando For, while e Condicionais
print("Menu:")
print("1. Contar de 1 a 5")
print("2. Sair")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    for i in range (1, 6):
        print(i)
elif opcao == "2":
    print("Saindo do programa.")
else:
    print("Opção inválida, tente novamente.")

    

#Atividade 09
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")
    
    if i == 15:
        print("Número 15 encontrado, interrompendo loop.")
        break


#Atividade 10
positivos = 0
negativos = 0
for i in range(10):
    numero =  float(input("Digite um número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        print("Número 0 inserido, interrompendo o loop.")
        break

print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")


#Atividade 11
for i in range (1, 30):
    print(i)

    if i % 5 == 0:
        print(f"{i} é múltiplo de 5")

    if i > 20: 
        print("Número maior que 20 encontrado, interrompendo o loop.")
        break

        '''
#Atividade 12
soma_preco = 0
for i in range(5):
    preco = float(input("Digite o preço do produto: "))
    soma_preco += preco

    if soma_preco > 100:
        print("Soma ultrapassou 100, interrompendo loop.")
        soma_preco *= 0.90 #Aplica desconto de 10%
        break

print(f"O total dos preços com desconto (se aplicável) é: {soma_preco:.2f}")