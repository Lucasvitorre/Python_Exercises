import math

cato= float(input('Insira o valor do cateto oposto: '))
cata= float(input('Insira o valor do cateto adjacente: '))

hip= math.hypot(cata,cato) #função matemática para calcular a hipotenusa

print(input(f'O comprimento da hipotenusa é igual a: {hip}'))

