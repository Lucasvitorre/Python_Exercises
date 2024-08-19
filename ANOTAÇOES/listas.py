#TUPLAS RAO REPRESENTADAS COM: () - SÃO IMUTAVEIS
'''
lanche = ("hamburguer","x-salada","pizza","pudim")
print(lanche)
lanche(3) = "picole"
print(lanche)

RESULTADO = TypeError: 'tuple' object is not callable
'''
#LISTAS SÃO REPRESENTADAS COM: []

lanche = ["hamburguer", "x-salada", "pizza", "pudim"]
print(lanche)
lanche[3] = "picole"
print(lanche)

#Adicionando ao final da lista mais um elemento:
lanche.append("Cookie")
print(lanche)
print #####
#Adicionando um objeto em determinadas posições:
lanche.insert(0,"Churrasco")
print(lanche)
#DICIONARIOS SÃO REPRESENTADOS COM: {}