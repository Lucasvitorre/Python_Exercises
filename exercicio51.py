#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
#NO FINAL MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

print('Gerador de Pogressão Aritmética')
print('#'*15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1

