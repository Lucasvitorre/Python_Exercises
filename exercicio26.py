#frase= str(input('Digite uma frase: ')).upper().strip()

#cont=frase.count('A')
#pos=frase.find('A')
#posr=frase.rfind('A')

#print(f'A letra A aparece {cont} vezes.')
#print(f'A primeira letra A apareceu na posição {pos+1}')
#print(f'A ultima vez que a letra A apareceu foi na posição: {posr})

    ########################################################################

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letra = str(input('Digite a letra que quer análisar: ')).upper().strip()
print(f'A letra {letra} apareceu {frase.count(letra)} vezes')
print(f'A primeira aparição da letra {letra} foi na {frase.find(letra)+1}° posição ')
print(f'A ultima vez que a letra {letra} apareceu foi na {frase.rfind(letra)+1}° posição')
