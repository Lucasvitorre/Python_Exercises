### Modo Simples
arquivo = open("primeiro_arquivo.txt", "a")
arquivo.write("Meu primeiro arquivo!m")
arquivo.close()

### Modo melhorado
with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\n Hakuna!!")