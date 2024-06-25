from datetime import date

atual = date.today().year
idade_maior= 0
idade_menor= 0


for seq in range (1,5):
    print(f"------{seq} PESSOA------")
    nome= input(f"Qual o nome da {seq}ª pessoa? ")
    idade = int(input(f"Qual a idade da(o) {nome}? "))
    sex = input("Sexo [M/F]: ")

med_idade = idade /4

print (med_idade)


