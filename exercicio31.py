#exercicio31

dist= int(input('Insira a distância da sua viagem em KM: '))


preco1= dist * 0.50
preco2= dist * 0.45

if dist <= 200:
    print(f'O preço da Viagem é de: R${preco1:.2f}')

else:
    print(f'O preço da Viagem é de: R${preco2:.2f}')

