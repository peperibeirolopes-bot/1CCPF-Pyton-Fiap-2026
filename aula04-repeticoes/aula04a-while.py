cp = 0
while cp < 10:
    cp += 1

    if cp == 3 or cp == 5:
        continue # Modificadores de fluxo

    if cp == 7:
        break # Modificadores de fluxo

    print(f"Produto {cp}")

# while decrescente de 4 ate 1
i = 4
while i > 0:
    print(i)
    i -= 1