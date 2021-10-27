import socket
host = 'localhost'
port = 6001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c, addr  = s.accept()
print ("Connection from :",str(addr))
c.send (b"Hello client, how are u")
msg = "Bye!"
c.send(msg.encode())
c.close()
