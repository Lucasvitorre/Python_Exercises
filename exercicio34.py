#exercicio34

sal= int(input('Insira o seu salário atualmente: '))


aum1= sal * 0.15
aum2= sal * 0.10

if sal <= 1250:
    print(f'O aumento salárial será de 15%: R${aum1:.2f}')

else:
    print(f'O aumento salarial será de 10%: R${aum2:.2f}')

