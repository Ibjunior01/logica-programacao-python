inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número inicial do intervalo: "))

soma_pares = 0
encontoru_par = False

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma_pares += 1
        encontoru_par = True

if encontoru_par:
    print(f" A soma dos números pares no intervalo de {inicio} a {fim} é: {soma_pares}!")
else:
    print(f"Não há números pares no intervalo de {inicio} a {fim}!")