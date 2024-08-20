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

#Removendo um objeto, diversas formas

del lanche[3]
lanche.pop(3) or lanche.pop() #Geralmente utilzado para remover o ultimo elemento, mas é possivel passar um elemento especifico.
lanche.remove("Churrasco") #Remover pelo conteúdo e náo pelo indice.
print(lanche)

if "Churrasco" in lanche:
    lanche.remove("Churrasco")

#DICIONARIOS SÃO REPRESENTADOS COM: {}