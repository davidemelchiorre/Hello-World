import socket

print "ZERO"

port = 9696
buflen=1024

print "A"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "B"
server.bind((socket.gethostname(), port))
print "C"
server.listen(1)
print "D"
while 1:
    print "In attesa di connessione..."
    
    print "E"

server.close()
