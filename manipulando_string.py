#FRASE DE TESTE
frase='Curso em Video Python'

#FATIAMENTO
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

#ANÁLISE
#comprimento da frase
len(frase)
#contar a quantidade de letras: ('a','r')
frase.count('o')
frase.count('o', 0,13) # fazendo fatiamento em conjunto com o count

#Procurar conjunto de string dentro da variavel
frase.find('deo')