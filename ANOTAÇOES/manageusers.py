from ANOTAÇOES.funcoes_fiap import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao=="E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios)
    input("Qual o usuário: ")