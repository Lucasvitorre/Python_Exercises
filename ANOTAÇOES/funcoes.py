
#CRIANDO FUNCOES PYTHON
def mostra_linha():
    print("")
    print("#"* 30)
    print("")

#CRIAND FUNCAO COM PARAMETRO
def linha1(msg):
    print("#"*30)
    print(msg)
    print("#"*30)
linha1("SISTEMA DE ALUNOS")

#PARTE PRATICA
def soma(a,b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}")

soma(103,150)

mostra_linha()

#EMPACOTAMENTO
def contador(*num):
    print(num)

mostra_linha()

contador(2,1,7)
contador(8,0)
contador(4,4,4,4,4,4,4)

#EXEMPLO DE LISTA DENTRO DE FUNCAO
def dobra(lst):
    pos =0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)

#DESEMPACOTAMENTO
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")

soma (8,9,10)

#AULA 2 DE FUNCOES ##

# INTERACTIVE HELP
##
##   BASTA SOMENTE UTILIZAR A FUNÇÃO HELP() no python

 #help(print) #direto no código

# DOCSTRINGS

###    DOCSTRINGS É UMA DOCUMENTAÇÃO QUE UTILIZA """ """


def contador (i,f,p):
    """
    --> FAZ uma contagem e mostra na tela.
        :param i: inicio da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}",end="")
        c += p
    print("Fim!")
help(contador)
contador(2,10,2)

# PARAMETROS OPCIONAIS
def somar(a,b,c=0): # Adicionar um parametro basta adicionar o operadorador dentro da funcao
    s = a+b+c
    print(f"A soma vale (S)")


somar(3,2,5)

# ESCOPO DE VARIAVEIS

    #Variavel Global ela está fora de uma função, e consegue ser acessada em qualquer lugar do programa.
    #Variavel Local está em uma função não é acessivel 
#Para ignorar a criação de uma variavel nova local basta escrever da seguinte forma dentro de uma função:
'''
def teste(b):
    global a 
    a=8
a=5
    
'''
# RETORNO DE RESULTADOS
def somar(a=0,b=0,c=0): # Adicionar um parametro basta adicionar o operadorador dentro da funcao
    s = a+b+c
    #Alterar o (print(f"A soma vale {s}")) para return
    return s

resp1 = somar(3,2,5)
resp2 = somar(1,7)
resp3 = somar(4)
print(f" Meus Calculos deram {resp1}, {resp2}, {resp3}.")

