#VARIAVEIS COM FOR-WHILE-IF-ELIF

#NESSE ARQUIVO ALGUNS EXEMPLOS DE IF-FOR-WHILE

#IF e ELIF

velocidade= int(input('Insira a velocidade:'))
multa= (velocidade-80)*7.00

if velocidade <=(80):#print (f'{num1}')
    print ('Não há multas para você!')

elif velocidade >(80):
    print('VOCE TOMOU UMA MULTA!!!!')
    print(f'O valor da multa é de:R${multa}')
    print('Dirija com atenção!')

#############################################################################################

#WHILE
# O WHILE É UM LAÇO INFINITO, ONDE O CÓDIGO SÓ ACABA DE SER EXECUTADO QUANDO TERMINA COM O RESULTADO ESPERADO.

velocidade = int(input('Insira a velocidade: '))

while velocidade > 80:
  multa = (velocidade - 80) * 7.00
  print(f"Você está acima da velocidade permitida! Multa: R${multa:.2f}")
  velocidade = int(input('Insira a nova velocidade: '))

print('Obrigado por dirigir com segurança!')

#############################################################################################

#WHILE COM BREAK
# COM O BREAK, O LAÇO SERÁ INTERROMPIDO.

velocidade = int(input('Insira a velocidade: '))

while True:
  if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f"Você está acima da velocidade permitida! Multa: R${multa:.2f}")
    break
  else:
    print('Você está dirigindo dentro da velocidade permitida!')
    break

    velocidade = int(input('Insira a nova velocidade: '))

print('Obrigado por dirigir com segurança!')

#############################################################################################

#WHILE COM CONTINUE:

velocidade = int(input('Insira a velocidade: '))

while True:
  if velocidade <= 0:
    print('Velocidade inválida. Digite novamente.')
    continue

  if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f"Você está acima da velocidade permitida! Multa: R${multa:.2f}")
  else:
    print('Você está dirigindo dentro da velocidade permitida!')

  velocidade = int(input('Insira a nova velocidade: '))

#############################################################################################
  
