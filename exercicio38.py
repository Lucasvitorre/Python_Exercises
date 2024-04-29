### PROGRAMA ANALISADOR DE NÚMEROS ###
import time

num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))

print ("#################################")
print("Analisando os números informado...")
print ("#################################")

if num1 == num2:
    print("Os dois números são iguais")

elif num1 > num2:
    print(f"O {num1} é maior do que {num2}.")

else:
    print(f"O número {num2} é maior do que o número {num1}.")