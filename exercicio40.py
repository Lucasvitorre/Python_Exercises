#MÉDIA NOTA#
import time
#import math

print("VALIDAÇÃO DE NOTA!")
time.sleep (3)

#credenciais
nome = input("Insira o seu nome completo: ")
ra = (input("Insira o seu RA: "))

#Notas
nota1 = float(input("Insira a sua nota da Atividade 1: "))
nota2 = float(input("Insira a sua nota da Atividade 2: "))
nota3 = float(input("Insira a sua nota da Atividade 3: "))
nota4 = float(input("Insira a sua nota da Atividade 4: "))

#calculo das notas das quatros primeiras atividades
nota_A01= nota1 + nota2 + nota3 + nota4 

#resultado calculo A01
print(f"{nome} a sua nota para a A01: {nota_A01}")

#calculo da nota geral da matéria
nota_A02 = float(input("Insira a sua nota da A2: "))
nota_final = nota_A01 + nota_A02

print(f"{nome} o valor da sua nota final para a matéria é: {nota_final}.")

if nota_final < 5:
    print("Com o resultado final das notas que você tirou você está REPROVADO.")

elif 5 >= nota_final <= 6.9:
    print("Com o resultado final das notas que você tirou você está em RECUPERAÇÃO.")

else:
    print("PARABÉNS, VOCÊ FOI APROVADO!!!")