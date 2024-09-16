all_dados= dict
const= "C"

def mostra_linha():
    print("")
    print("#"* 30)
    print("")
    
def dados():
    nome= input("Insira o seu nome: ")
    idade = int(input("Insira o sua idade: "))
    sexo = input("Digite o seu sexo: (M/F): ").upper()
    #CRIAÇÃO DE UM DICIONARIO
    dados_preenchidos = {"nome":nome,"idade":idade,"sexo": sexo}
    #PREENCHIMENTO DOS DADOS EM UMA LISTA
    all_dados.copy(dados_preenchidos)
    
while const == "C":
    dados()
    mostra_linha()
    print("Gostaria de continuar?")
    const = input("Digite 'C' para Continuar ou 'P' para Parar o script: ").upper()
    mostra_linha()

    if const == "P":
        print(all_dados.values())
        break
