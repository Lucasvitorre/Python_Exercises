#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

print("Programa Tabuada 2.0")

num = int(input("Insira o valor: "))
for tabuada in range (1, 10 + 1):
    tab = tabuada * num
    print(f"{num} x {tabuada} = {tab}")

print("FIM")