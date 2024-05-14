#Estrutura de repetição

#FOR sendo fazer o código passo 1 a 10 e fora do for fazendo o passo pega.
for c in range(1,10):
    passo
pega


#FOR realiza 3 vezes os passos como laço
for c in range(0,3):
    passo 
    pula
passo
pega

FOR COM VARIAVEIS IF/ELSE.
for c in range(0,3):
    if moeda:
       pega
    passo
    pula
passo
pega

#########################################################################################

for repeticao in range(6, 0, -1):
    print(repeticao)
print("Fim")

###########################################################################################

#CONTADOR CONDICIONAL AO VALOR DA VARIAVEL
n= int(input("Digite um número: "))
for c in range(0, n+1):
    print (c)
print("FIM")

#CONTADOR CONDICIONAL AO VALOR DE INICIO FIM E PASSO
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM")

#CONTADOR CONDICIONAL DENTRO DO FOR

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print(f"A soma dos números inseridos é de: {s}")