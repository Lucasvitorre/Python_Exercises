#PROGRAMA PARA CALCULAR MULTA

print('CALCULAR MULTA')

velocidade= int(input('Insira a velocidade:'))
multa= (velocidade-80)*7.00

if velocidade <=(80):#print (f'{num1}')
    print ('Não há multas para você!')

elif velocidade >(80):
    print('VOCE TOMOU UMA MULTA!!!!')
    print(f'O valor da multa é de:R${multa}')
    print('Dirija com atenção!')