import socket
resp = "s"
while (resp == "s"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente a url informada é: ", ip)
    resp = input("Digite <s> para continuar: ")