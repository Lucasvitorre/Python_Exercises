equipamento = []
valores = []
seriais = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamento.append (input("Equipamento: "))
    valores.append (float(input("Valor: ")))
    seriais.append (input("Serial Number: "))
    departamento.append (input("Departamento: "))
    resposta = input ("Digite \"S\" para continuar: ").upper()

busca = input("\n Digite o nome do equipamento que deseja buscar: ")
for indice in range (0 , len (equipamento)):
    if busca==equipamento[indice]:
        print("Valor..:", valores[indice])
        print("serial..:", seriais[indice])