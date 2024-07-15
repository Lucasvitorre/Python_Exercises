from time import sleep

numero = int(input("Digite um número: "))
while numero < 100:
    print(str(numero))
    numero = numero + 1
    sleep(0.5)
print("Laço encerrado....")