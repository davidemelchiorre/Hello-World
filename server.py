import socket

HOST = ''
PORT = 9696
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "Connected by", addr
while 1:
    data = conn.recv(1024)
    if not data:break
    print"Ricevuto:",data.decode('utf-8')
    conn.send(data)
conn.close()
