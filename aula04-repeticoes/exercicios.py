#ex 1
while True:
    print("Olá, Mundo")

    resposta = input("Deseja exibir a mensagem novamente? (sim/não): ")

    if resposta.lower() != "sim":
        break

print("Fim")

#ex 2

for i in range(0, 101, 10):
    print(i)


# ex 3

n = int(input("Digite um número: "))

for i in range(0, 26):
    print(f"{n} x {i} = {n * i}")


# ex 4

soma = 0
for i in range(0, 5):
    valor = int(input("Digite um valor: "))
    soma += valor
print(f"Soma: {soma}")


# ex 5

n = int(input("Digite um valor: "))
for i in range(2, n+1, 2):
    print(i)


# ex 6

maior = int(input("Digite um valor: "))
for i in range(0, 4):
    valor = int(input("Digite um valor: "))
    if valor > maior:
        maior = valor
print(f"Maior: {maior}")

# ex 7

n = int(input("Digite um número positivo: "))
while n <= 0:
    n = int(input("Digite um número positivo: "))
soma = 0
for i in range(1, n+1):
    soma += i
print(f"A soma de 1 até {n} é: {soma}")

# ex 8

n = int(input("Digite um número: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# ex 9

for n in range(2, 2001):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n)