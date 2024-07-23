#CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO.
#O PROGRAM SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, Q É A CONDICAO DE PARADA.
# NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
#(DESCONSIDERANDO A FLAG)

n = s = c = 0
while True:
    n = int(input("Insira o valor: "))
    if n == 999:
        break
    s+=n
    c+=1
print(f"O valor da soma é: {s}")
print(f"A quantidades de números inseridos foi: {c}")