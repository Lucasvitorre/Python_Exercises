#------------------------------------------Condição Simples-----------------------------------------------------
nome = str(input("Qual o seu nome? "))

if nome == "Gustavo":
    print (f"Bem vindo ao sistema {nome}!")
#---------------------------------------------------------------------------------------------------------------
elif nome == "Gu" or nome == "Gus":
    print("Seu nome está proximo do nome correto.")

#------------------------------------------Condição Composta-----------------------------------------------------
else:
    print("Seu nome não é o correto para acesso!")
#------------------------------------------Condição Aninhadas-----------------------------------------------------
    