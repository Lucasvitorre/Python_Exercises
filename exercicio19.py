import random

nome1= input('Insira o nome dos alunos: ') 
nome2= input('Insira o nome dos alunos: ') 
nome3= input('Insira o nome dos alunos: ')
nome4= input('Insira o nome dos alunos: ')

nomes= [nome1,nome2,nome3,nome4]

alu_esc= random.choice(nomes)

print(f'O aluno escolhido foi: {alu_esc}')
