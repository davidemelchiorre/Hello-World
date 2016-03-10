import socket

port = 9696
buflen=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), port))
server.listen(1)
while 1:
    print "In attesa di connessione..."
    client, buf = server.accept()
    #-------------------------
    buf = client.recv(buflen)
    if not buf:break
    cmd=buf.decode('utf-8')
    client.send(bytes(0))
    #--------------------------
    buf = client.recv(buflen)
    if not buf:break
    arg=buf.decode('utf-8')
    client.send(bytes(0))
    #--------------------------
    print cmd," ",arg
    if cmd=="close" and arg=="socket":
        client.close()
        server.close()
    if cmd=="close" and arg=="client":
        client.close()
client.close()
server.close()
