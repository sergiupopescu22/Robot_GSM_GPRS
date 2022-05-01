import socket

#host = ''
#host = '192.168.88.254'
#host = '86.125.92.13'
#host = '172.20.152.91'
#host = socket.gethostbyname(socket.gethostname())

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
comanda_robot = ""

print(host , port)
print("The server is listening......")

while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    try:
        data = conn.recv(1024)
        if not data:
            break
        else:
            if data.decode('UTF-8').find("Controller:") != -1:
                print("Controller Client Says: " + data.decode('UTF-8')[11:])
                comanda_robot = data.decode('UTF-8')[11:]
                conn.sendall(b'Server received the command')
            elif  data.decode('UTF-8').find("Robot:Request Command") != -1:
                conn.sendall(comanda_robot.encode('ascii'))
    except socket.error:
        print("Error Occured.")
        break

    conn.close()