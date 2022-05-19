import socket

#host = '192.168.88.48'#$socket.gethostname()
#host = '10.172.248.178'
#host = '169.254.89.142'
#host = '172.104.230.27'
host = '192.168.88.254'
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))