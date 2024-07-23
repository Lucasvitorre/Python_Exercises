# while 
'''
cont = 1
while cont <= 10:
    print(cont,",", end ="")
    cont += 1
print("Acabou")
'''
####
# while sem fim até encontrar um valor de n=999
'''
n = 0
while n != 999:
    n = int(input("Digite um número: "))
'''   
###
# while com contador até 5 inserções de valor ou alternativa
'''
n = cont = 0
while cont < 5:
    n = int(input("Digite um número: "))
    cont += 1
'''
### Forma incorreta de utilizar o while, pois há a soma da flag 999
'''
n = s = 0
while n != 999:
    n = int (input("Digite um número: "))
    s += n
s-= 999 # ERRADO POR SER GAMBIARRA 
print(f"A soma vale {s}")]
'''
## UTILIZANDO BREAK DE FORMA CORRETA

n= s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")
