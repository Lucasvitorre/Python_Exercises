from time import sleep
import math

print("PROGRAMA PARA VERIFICAR A MEDIA.")
print("---*"*15)

print("Insira o valor que de deseja:")
num1 = int(input(""))

while num1 !=0:
    num1 = int(input(""))
    print("Você quer continuar?")
    cause = input ("")
    if cause == "SIM":
        print