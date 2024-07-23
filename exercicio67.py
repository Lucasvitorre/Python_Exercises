#FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO
#O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO
tabuada = 0

while True:
    tabuada= int(input("Qual tabuada você quer saber? "))
    print("-"*20)
    for count in range(10):
        resultado = tabuada * count+1
        print(f"{tabuada} x {count +1 } = {resultado}" )

    if tabuada < 0:
        break
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")