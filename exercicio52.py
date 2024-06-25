#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")