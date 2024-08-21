#TUPLAS RAO REPRESENTADAS COM: () - SÃO IMUTAVEIS
'''
lanche = ("hamburguer","x-salada","pizza","pudim")
print(lanche)
lanche(3) = "picole"
print(lanche)

RESULTADO = TypeError: 'tuple' object is not callable
'''
## LISTAS SÃO REPRESENTADAS COM: []

lanche = ["hamburguer", "x-salada", "pizza", "pudim"]
print(lanche)
lanche[3] = "picole"
print(lanche)

## Adicionando ao final da lista mais um elemento:
lanche.append("Cookie")
print(lanche)
print #####

## Adicionando um objeto em determinadas posições:
lanche.insert(0,"Churrasco")
print(lanche)

## Removendo um objeto, diversas formas

del lanche[3]
lanche.pop(3) or lanche.pop() #Geralmente utilzado para remover o ultimo elemento, mas é possivel passar um elemento especifico.
lanche.remove("Churrasco") #Remover pelo conteúdo e não pelo indice.
print(lanche)

if "Churrasco" in lanche: # Remover um conteudo sem precisar necessáriamente um erro 
    lanche.remove("Churrasco")

## CRIAR LISTA EM ESTRUTURA DE RANGES
valores=list(range(4,11))
print(valores)

## CRIAÇÃO DE LISTA COM VALORES
valores = [8,5,3,2,4,5,1,6]
print(valores)
valores.sort() # ORDENA OS VALORES CORRESPONDENTES A VARIAVEL.
valores.sort(reverse=True) # Inverso
print(len(valores)) #Quantidade de valores
print(valores) 

## EXEMPLOS DA AULA 
print("##################################") 
print("")
 
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("cheguei ao final da lista.")

