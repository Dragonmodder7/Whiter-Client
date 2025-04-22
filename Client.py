import socket

HOST = 'SEU_IP_AQUI'
PORT = 4444

def banner():
    print("""
██╗    ██╗██╗  ██╗██╗████████╗███████╗██████╗     
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔══██╗    
██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝    
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗    
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
     W H I T E R   C L I E N T   V2.1
""")

def menu():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(s.recv(2048).decode())

    while True:
        print("\n[ MENU ]")
        print("1 - Enviar comando")
        print("2 - Sair")
        op = input("> ")

        if op == "1":
            comando = input("Comando > ")
            s.send(comando.encode())
            resposta = s.recv(4096).decode()
            print(resposta)
        elif op == "2":
            s.send(b"exit")
            break
        else:
            print("Opção inválida.")
    s.close()

banner()
menu()
