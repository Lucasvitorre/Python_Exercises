from time import sleep

print("----"*15)
print("Bem vindo ao seu sistema")
print("----"*15)
num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))

mult = num1 * num2 
soma = num1 + num2

action = 0
while action != 5:  
    print('''Escolha o que fazer com os números inseridos:
          [1] SOMAR
          [2] MULTIPLICAR
          [3] MAIOR NÚMERO
          [4] NOVOS NÚMEROS
          [5] SAIR DO PROGRAMA''')
    
    action = int(input("Insira a opção desejada: "))

    if action == 1:
        print(f"A soma dos números é: {soma}")
        print("----"*15)
        print("----"*15)

    elif action == 2:
        print(f"A multiplicação dos números é: {mult}")
        print("----"*15)
        print("----"*15)
        
    elif action == 3:
        if num1 > num2:
            print(f"O {num1} é o número maior!")
        else:
            print(f"O {num2} é o número maior!")
            print("----"*15)
            print("----"*15)

    elif action == 4:
        print("Insire os valores novamente...")
        num1 = int(input("Insira o primeiro: "))
        num2 = int(input("Insira o segundo: "))
        print("----"*15)
    elif action == 5:
        print("Obrigado por utilizar o sistema!")

    else:
        print('Opção inválida, tente novamente!')
        print("----"*15)
        print("----"*15)
    sleep(2)


