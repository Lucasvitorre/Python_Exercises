import random
#import 

print ('PROGRAMA ESCOLHA UM NÚMERO, ENTRE 0 E 10')

num1= random.randrange(11)
#print (f'{num1}')

escolha1= int(input('Insira o número que você acredita ser o certo:'))

if num1 == escolha1:
    print('VOCÊ ESCOLHEU O NÚMERO CERTO, PARABÉNS!!!')

else:
    print('VOCÊ ERROU, TENTE NOVAMENTE!')

#print (f'{num1}')