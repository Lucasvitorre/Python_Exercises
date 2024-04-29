print("ANALISADOR DE ALISTAMENTO.")

idade= int(input("Insira a sua idade: "))
tempo_faltante = 18 - idade
tempo_excedente = idade - 18

if idade <= 17:
    print("Você não tem idade para se alistar ainda!")
    print(f"Ainda falta {tempo_faltante} ano(s) para você se alistar. ")

elif idade == 18:
    print("Você tem que se alistar nesse ano, fique atento aos proximos passos!")

else:
    print("Você deixou passar a data para alistamento, tome as devidas providências.")
    print(f"O tempo que você deixou de ser alistar é de {tempo_excedente} ano(s).")