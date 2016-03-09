import socket

port = 9696
buflen=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), port))
server.listen(1)
client, buf = server.accept()
while 1:
    buf = client.recv(buflen)
    if not buf:break
    cmd=data.decode('utf8')
    print("CMD=",cmd)
    client.send("ack".encode('utf8'))
client.close()
