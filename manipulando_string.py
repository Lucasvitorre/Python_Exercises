#FRASE DE TESTE
frase='Curso em Video Python'

###------------FATIAMENTO-------------------###
#SOMENTE UMA LETRA
frase[9]

#intervalo entre o 9 e o 12
frase[9:13]

#tudo até o 12º indice 
frase[:13]

#tudo depois do 14º indice
frase[14:]

#pulando de dois em dois
frase[9:13:2] 

#pulando de três em três até o final da frase
frase[9::3]

###-------------ANALISE-------------###
#Quantidade de caracteres na frase
len(frase)

#contar a quantidade de letras: ('a','r')
frase.count('o')
#faz fatiamento em conjunto com o count
frase.count('o', 0,13)

#Procurar conjunto de string dentro da variavel
frase.find('deo')

#Valor boolean se há ou não a palavra na variavel.
'Curso' in frase

###-------------TRANSFORMAÇÃO--------------###
#Alteração de strings
frase.replace('Python','Android')

#TODAS MAIUSCULAS
frase.upper()

#TODAS MINUSCULAS
frase.lower()

#Somente o primeiro caracter em maiusculo
frase.capitalize()

#Todas as palavras após espaço em maiusculo
frase.title()

#Retirar todos espaços de frase 
frase.strip
frase.rstrip #espaços a direita
frase.lstrip #espaços a esquerda

###-------------Divisão--------------###
#Divide por espaços
frase.split()

###-------------Junção--------------###
'-'.join(frase)


