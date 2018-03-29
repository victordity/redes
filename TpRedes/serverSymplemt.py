from socket import *
import threading

#Classe que gera os clientes
class CLiente(threading.Thread):
    def __init__(self,c,server,port, *menssagem):
        # Numero de identificacao com o cliente
        self.c = c

        # Servidor a ser conectado
        self.server = server

        # Porta a ser usada
        self.port = port

        # Menssagens a serem colocadas
        self.msgs = menssagem

        threading.Thread.__init__(self)

    def run(self):
        #Criamos o socket e o conectamos ao servidor
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.server,self.port))







# Nome do host
host = '127.0.0.1'

# Porta para o host se conectar
server_port = 5152

#Cria um objeto socket
s = socket(AF_INET, SOCK_STREAM)

#Vincula o servidor a porta indicada
param = host,server_port
s.bind(param)


s.listen(5)

while True:


    print('Esperando conexao')
    conexao, endereco = s.accept()
    print("Server conectado por",endereco)

    while True:
        #Recebe data enviada pelo cliente
        data = conexao.recv(1024)

        #Se enviar um dado vazio o programa para
        if not data: break

        #O servidor manda de volta a mensagem
        conexao.send(b'Eco=>'+ data)

    conexao.close()

