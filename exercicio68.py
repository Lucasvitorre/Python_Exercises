import random
while True:

    num1 = int(input("Digite o número: "))
    num2 = random.randint(0,20)
    soma = num1 + num2 

    escolha = input(str("Par ou Impar? [P/I]: "))
    sair = input("Deseja continuar? ").upper()
    print(sair)
    if sair == "NAO":
        break
