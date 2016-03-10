import socket

host=''
port = 9696
buflen=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, buf = server.accept()
buf = client.recv(buflen)
cmd=buf.decode('utf-8')
print cmd
client.close()
