import random
while "impar":
    num1 = int(input("Digite o número: "))
    num2 = random.randint(0,20)
    soma = num1 + num2 


    escolha = input("Par ou Impar? [P/I]: ")

print(f"Você escolheu {num1} e o computador {num2}, o valor da soma é {soma}.")
