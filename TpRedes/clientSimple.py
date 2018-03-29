# coding=utf-8
from socket import *
import sys

#host = '127.0.0.1'
host = sys.argv[1]
#server_port = 5152
server_port = int(sys.argv[2])
msg = bytes(sys.argv[3])

# Mensagem a ser enviada em bytes
msg = bytes(sys.argv[3])

# criamos o socket e o conectamos ao servidor
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, server_port))

# Mandamos a mensagem
s.send(msg)

data = s.recv(1024)
print('Cliente recebeu: ', data)


s.close()
