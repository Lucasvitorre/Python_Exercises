#import random
#nome1= input('Insira o nome dos alunos: ') 
#nome2= input('Insira o nome dos alunos: ') 
#nome3= input('Insira o nome dos alunos: ')
#nome4= input('Insira o nome dos alunos: ')
#nomes= [nome1,nome2,nome3,nome4]
#aluno_esc= random.shuffle(nomes,k=4(nomes))
#print(f'O aluno escolhido foi: {alu_esc}')

import random

# Solicitar os nomes dos alunos
nome1 = input('Insira o nome do primeiro aluno: ')
nome2 = input('Insira o nome do segundo aluno: ')
nome3 = input('Insira o nome do terceiro aluno: ')
nome4 = input('Insira o nome do quarto aluno: ')

# Criar uma lista com os nomes dos alunos
lista_de_nomes = [nome1, nome2, nome3, nome4]

# Embaralhar a lista de nomes
random.shuffle(lista_de_nomes)

# Escolher um nome aleatório da lista embaralhada
aluno_escolhido = random.choice(lista_de_nomes)

print("Lista de nomes em ordem aleatória:", lista_de_nomes)