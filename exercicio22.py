#PROGRAMA PARA LER AS INFORMAÇÕES
nome= str(input('Insira o seu nome: '))
nomed= len(nome.replace(' ',''))
fnome= nome.split()
fnome1= len(fnome)

print (f'O nome em letra maiuscula é: {nome.upper()}')
print (f'O nome em letra minuscula é: {nome.lower()}')
print (f'A quantidade de caracteres no nome é de: {nomed}')
print (f'O primeiro nome contém: {fnome1}')
