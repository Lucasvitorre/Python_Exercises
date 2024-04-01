num1= int(input('Insira o primeiro número: '))
num2= int(input('Insira o segundo número: '))
num3= int(input('Insira o terceiro número: '))

menor = num1

if num2<num1 and num2<num3:
    menor= num2
if num3<num1 and num3<num2:
    menor = num3


maior = num1
if num2>num1 and num2>num3:
    maior= num2
if num3>num1 and num3>num2:
    maior = num3
print(f'O maior número digitado foi:{maior}')
print(f'O menor valor digitado foi {menor}')