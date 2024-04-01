#EXERCICIO 30

num1 = int(input("Insira qualquer valor para saber se é par ou impar: "))
resto = num1 % 2

while True:
    if resto == 0:
        print("Número é par")
        break
    else:
        print("Número é impar")
        break
 
