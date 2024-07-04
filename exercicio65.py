from time import sleep
import math

print("PROGRAMA PARA VERIFICAR A MEDIA.")
print("---*"*15)


num1 = []



while num1 !=999:
    print("Insira o valor que de deseja:")
    num1 = int(input(""))
    print("Você quer continuar?")
    cause = input ("").upper()
    
    if cause == "SIM":
        print("---"*15)
    elif cause == "Não":
        quant = num1.count(int)
        print(quant)
    else:
        print("Obrigado")
