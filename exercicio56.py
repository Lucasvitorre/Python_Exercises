from datetime import date
#import 

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20= 0

for seq in range (1,5):
    print(f"------{seq} PESSOA------")
    nome= input(f"Qual o nome da {seq}ª pessoa? ")
    idade = int(input(f"Qual a idade da(o) {nome}? "))
    sex = input("Sexo [M/F]: ")
    somaidade += idade
    if seq == 1 and sex in "Mm" :
        maioridadehomem = idade
        nomevelho = nome
    if sex in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sex in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade /4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O home mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f"Ao todo temos {totmulher20} mulher com menos de 20 anos.")