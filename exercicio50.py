#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELAS QUE FOREM PARES.
#SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O.
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        print('A soma dos números pares é {}'.format(soma))