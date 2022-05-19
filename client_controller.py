import socket
#host = '192.168.88.254'
host = '172.104.230.27'
port = 12345



option = -1

while option != 0:
    print("-------------------------------------")
    print("List of commands:")
    print(" 0) Exit")
    print(" 1) Start")
    print(" 2) Stop")
    print(" 3) Move Froward")
    print(" 4) Move Back")
    print(" 5) Turn Right")
    print(" 6) Turn Left")
    print("")
    print("Choose a command: ")
    option = int(input())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    if option == 0:
        break
    elif option == 1:
        s.sendall(b'Controller:Start')
    elif option == 2:
        s.sendall(b'Controller:Stop')
    elif option == 3:
        s.sendall(b'Controller:Move Froward')
    elif option == 4:
        s.sendall(b'Controller:Move Back')
    elif option == 5:
        s.sendall(b'Controller:Turn Right')
    elif option == 6:
        s.sendall(b'Controller:Turn Left')

    data = s.recv(1024)
    print('Received', repr(data))

    s.close()


