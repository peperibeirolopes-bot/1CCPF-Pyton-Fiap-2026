#ex 1

import random
n = int(input("Digite n: "))
vetor = []
for i in range(0, n):
    vetor.append(random.random())
for i in range(0, n):
    print(vetor[i])

# ex 2

n = int(input("Digite o número de alunos: "))
notas = []
soma = acima = abaixo = igual = 0
for i in range(n):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma += nota
media = soma / n
for nota in notas:
    if nota > media:
        acima += 1
    elif nota < media:
        abaixo += 1
    elif nota == media:
        igual += 1
print(f"Média: {media}")
print(f"Acima: {acima}")
print(f"Abaixo: {abaixo}")
print(f"Igual: {igual}")

# ex 3

meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(0, 12):
    print(f"O mês de {meses[i]} tem {dias[i]} dias ao todo.")


#ex 4

n = int(input("Digite n: "))
vetor = []
soma = 0
for i in range(n):
    numero = int(input("Digite um número: "))
    vetor.append(numero)
for numero in vetor:
    soma += numero
print(f"Soma: {soma}")

# ex 5

nomes = []
while True:
    nome = input("Digite um nome: ")
    if nome == "":
        break
    nomes.append(nome)
for nome in reversed(nomes):
    print(nome)

# ex 6
