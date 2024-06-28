#VALIDADOR DE IDENTIDADE
#AUTOR: @lucasvitorre

sexo = "F" or "M"

'''while sexo:
    print("Digite seu sexo: [M/F]")
    sexo_cliente = input()
    if sexo_cliente == "M" or sexo_cliente == "F":
        print("Sexo válido, obrigado pelas confirmações")
        break
    '''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")