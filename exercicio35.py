#exercicio35

print('-='*20)
print('Analisador de triângulos.')
print('-='*20)

r1=float(input('Insira o valor da 1 reta:'))
r2=float(input('Insira o valor da 2 reta:'))
r3=float(input('Insira o valor da 3 reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!!!')

