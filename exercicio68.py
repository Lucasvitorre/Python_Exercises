import random
while True:
    nome= input("Insira o seu nome: ")
    user = int(input(f"{nome}, digite um número: "))
    pc = random.randint(0,20)
    soma = user + pc
    
    escolha = input(str("Par ou Impar? [P/I]: "))
    
    if soma % 2 == 0:
        
    
           
    

    sair = input("Deseja continuar? ").upper()
    print(sair)
    if sair == "NAO":
        break
