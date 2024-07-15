##################EXEMPLOS-CONDICOES##############################

nome= str(input('Insira o seu nome:'))
sobrenome= str(input('Insira o seu sobrenome:'))
lista= []

if nome:
    print ('A variavel nome não é vazia')

if nome:
    print('A variavel sobrenome não é vazia')

##################################################################

##################-OPERADORES-LOGICOS-##############################

variavel=

if nome:
    print('A variavel nome não é vazia')

if nome == #IGUAL
if nome != #DIFERENTE
if nome >= #Maior ou igual
if nome <= #Menor ou igual
if nome > #Maior
if nome < #Menor
if a in nome #Está dentro
if a in lista
if is true #É verdadeiro
if True

#################-ELSE-####################

valor1= int(input('Insira o primeiro valor: '))
valor2= int(input('Insira o segundo valor: '))

if valor1 > valor2:
    print ('O primeiro valor é maior do que o segundo valor')

else:
    print ('O segundo valor é maior do que o primeiro valor')

#################-ELIF-####################

cor = str(input('Insira a cor:'))

if cor == 'Verde':
    print('Acelerar')
elif cor == 'Amarelo':
    print('Atenção')
else:
    print ('Parar')

##########-IF-COM-FOR##############

lista = ['Heitor','Daniel','Lira']

for item in lista:
    if item == 'Daniel':
        print('É Daniel')
    else:
        print('Não é Daniel')