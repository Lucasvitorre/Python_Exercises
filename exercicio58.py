import random
import time

"""
print("Sou seu computador...")
time.sleep(1)
print("Pensei em um número entre 0 e 10.")
time.sleep(1)
print("Será que você consegue adivinhar qual foi?")
time.sleep(1)

numero_sorteado= random.randint(0,10)

palpite = int(input("Qual o seu palpite: "))
while palpite != numero_sorteado:
    palpite= int(input("O número está incorreto, tente novamente: "))

print(f"PARABÉNS VOCÊ ACERTOU O {numero_sorteado} E ESTÁ PRONTO PARA A PROXIMA FASE!!!!")
"""

from random import randint
computador = randint(0,10)
print("Olá, Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
            
print(f"Acertou com {palpites} tentativas. Parabéns!")
