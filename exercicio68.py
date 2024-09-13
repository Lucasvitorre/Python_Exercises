import random

nome = input("Insira o seu nome: ")

qtd = 0  # Contador de vezes que o loop foi executado
vitorias = 0  # Contador de vitórias

while True:
    user = int(input(f"{nome}, digite um número: "))
    pc = random.randint(0, 20)
    soma = user + pc

    escolha = input(str("Par ou Ímpar? [P/I]: ")).upper()

    if soma % 2 == 0:
        print(f"O número sorteado é: {soma} Par!")
        if escolha == "P":
            print("VOCÊ GANHOU!!!")
            vitorias += 1  # Incrementa o número de vitórias
            print("#"*20)
        else:
            print("Você perdeu!!!")
            break
    elif soma % 2 != 0:
        print(f"O número sorteado é: {soma} Ímpar!")
        if escolha == "I":
            print("VOCÊ GANHOU!!!")
            vitorias += 1  # Incrementa o número de vitórias
            print("#"*20)
        else:
            print("Você perdeu!!!")
            break
    
    qtd += 1  # Incrementa o contador de execuções do loop
print("#"*20)
print(f"Fim do jogo! Você venceu {vitorias} vezes.")
