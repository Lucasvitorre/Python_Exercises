
num1= int(input("Digite um número inteiro:"))

print("""Escolha uma das bases para conversão:
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL""")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num1} convertido para BINÁRIO é igual a {bin(num1)}")

elif opcao ==2:
    print(f"{num1} convertido para OCTAL é igual a {oct,(num1)}")

elif opcao ==3: 
    print(f"{num1} convertido para HEXADECIMAL é igual a {hex,(num1)}")

else:
    print("Opção inválida. Tente novamente!")