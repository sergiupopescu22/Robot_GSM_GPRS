import socket
import time
#host = '192.168.88.254'
host = '172.104.230.27'
port = 12345

print("Robotul receptioneaza ultima comanda trimisa de controller.....")

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'Robot:Request Command')
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()

    time.sleep(0.5)