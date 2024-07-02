from time import sleep

print("----"*15)
print("Bem vindo ao sistema de agendamento!!")
print("----"*15)
nome = str(input("Insira o seu nome: "))

action = 0
while action != 4:  
    print('''O que você deseja realizar:
          [1] AGENDAMENTO
          [2] REAGENDAMENTO
          [3] CANCELAMENTO
          [4] SAIR DO AGENDAMENTO''')

    print("Insira a opção desejada.")
    
    action = int(input("Opção: "))

    if action == 1: 
        data = int(input("Data: "))
        hora = int(input("Insira a hora: "))
        minuto= int(input("Insira os minutos: "))
        print("Insira o que irá fazer: Ex: "Cabelo + Barba ou Cabelo" "))

def create_event(service):
    event= {
        "summary": f"Agendamento {nome}",
        "description": f"{modo}"
        }

   
        print("Teste")
        #codigo de inclusao de um evento google calendar

    if action == 2:
        print("Vamos verificar se há a disponibilidade.")
        data = int(input("Insira a Data: "))
        hora = int(input("Insira a hora: "))
        minuto= int(input("Insira os minutos: "))
        
    if action == 3:
        print("Você tem certeza, que deseja cancelar o seu horário?")
        cancel = input("Insira SIM OU NAO: ")
        if cancel == "NAO":
            print("Muito Obrigado pela preferência, aguardamos a sua visita!")
        else:
            #Codigo de exclusao do evento
            print("Esperamos você hoje")
            
    if action == 4:
        print("Obrigado por utilizar o sistema de agendamento!")
