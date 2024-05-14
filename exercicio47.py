from time import sleep
import math

#CRIE UM PROGRAMA QUE MOSTRE NA TELA "TODOS OS NÚMEROS PARES" QUE ESTÃO NO INTERVALO ENTRE 1 E 50.

for intervalo in range (1, 50):
    if intervalo % 2 == 0:
        sleep(1)
        print(f"Os números pares são: {intervalo}")
print (f"Esse são os números pares para o intervalo de 1 a 50!")