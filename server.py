import socket

addr = ''
port = 9696
buflen=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, port))
server.listen(1)
conn, buf = server.accept()
while 1:
    buf = conn.recv(buflen)
    if not buf:break
    cmd=data.decode('utf8')
    print("CMD=",cmd)
    conn.send("ack".encode('utf8'))
conn.close()
