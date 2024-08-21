from funcoes import mostra_linha

dados=dict()
dados = {"nome":"Pedro","idade":"25"}  #INCLUINDO AS CHAVES MAIS VALORES 
print(dados["nome"])
dados["sexo"]= "M"  #COMANDO PARA ADICIONAR CHAVES 
print(dados)
del dados["idade"] #COMANDO PARA EXCLUIR CHAVES 
print(dados)

mostra_linha()
filme = {
    "titulo":"Star Wars",
    "Ano":"1977",
    "Diretor":"George Lucas"    
    }
print(filme.keys())
print(filme.values())
print(filme.items())
mostra_linha()

# USANDO ITEMS
for k, v in filme.items():
    print(f"o {k} é {v}")
print("")
#EXEMPLO DE LISTAS COM DICIONARIOS
bras = []
est1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
est2 = {"uf": "Sao Paulo", "sigla": "SP"}
bras.append(est1)
bras.append(est2)

print(bras)

mostra_linha()

#OUTRO EXEMPLO
estado = dict()
brasil = list()

for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) # METODO DE COPIA DICIONARIO
for e in brasil:
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}.")