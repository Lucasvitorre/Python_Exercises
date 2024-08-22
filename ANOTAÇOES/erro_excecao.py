try: #ELE TENTA O CÓDIGO 
    a = int(input("Insira um número: "))
    b = int(input("Insira um número: "))
    re = a/b
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero!")

except: #SE OCORRER ALGUM ERRO O QUE ESTÁ DENTRO DO EXCEPT SERÁ MOSTRADO.
    #É POSSIVEL CRIAR MUITOS EXCEPT ATÉ OS ELSE
    print("Infelizmente tivemos um problema!")
    
else: #SE OCORRER TUDO CERTO, IMPRIMIRA O QUE ESTÁ DENTRO DO ELSE
    print(f"{re:1f}")

finally: #OCORRE MESMO SE DER ERRADO OU CERTO!
    print("Volte sempre muito obrigado!")
