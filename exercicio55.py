maior= 0
menor= 0

for seq in range(1,6):
    peso = float(input(f"Peso da {seq}° pessoa: "))
    if seq == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    print(14*"====")

print(f"O maior peso lido foi:{maior}kg.")
print(f"O menor peso lido foi:{menor}kg.")
