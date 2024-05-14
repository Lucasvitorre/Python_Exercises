#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Inicializando a variável para armazenar a soma
soma = 0

# Loop de 1 até 500, com passo de 2 para garantir que estamos apenas nos números ímpares
for num in range(1, 501, 2):
    # Verifica se o número é ímpar e múltiplo de 3
    if num % 2 != 0 and num % 3 == 0:
        # Adiciona o número à soma
        soma += num

# Imprime o resultado
print("A soma dos números ímpares múltiplos de três entre 1 e 500 é:", soma)
