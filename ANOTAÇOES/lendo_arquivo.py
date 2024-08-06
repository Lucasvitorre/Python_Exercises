with open (r"C:\Users\70159006\OneDrive - ArcelorMittal\Documentos\GitHub\Python\ANOTAÇOES\primeiro_arquivo.txt", "r") as arquivos:
    #Formas de visualizar
    #mostra todo o conteudo
    #conteudo = arquivos.readline()

    #Outra forma de imprimir linha por linha
    for linha in arquivos.readlines(): 
        print(linha)

