
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

#EXEMPLO
def dobra(lst):
    pos =0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)