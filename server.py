import socket
from add import add
from multiplication import mult

def server():
    hosted_services=['add','mult']
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocket.bind(("localhost",5500))
    serversocket.listen(5)
    print("RPC Server Listening")
    while 1:
        (clientsocket,address) = serversocket.accept()
        data=clientsocket.recv(1024).decode()

        print(data)
        inp= data.split(",")
        if inp[0] in hosted_services:
            if inp[0] == "add":
                clientsocket.send(str(add(int(inp[1]),int(inp[2]))).encode())
            elif inp[0] == "mult":
                clientsocket.send(str(mult(int(inp[1]),int(inp[2]))).encode())
        else:
            clientsocket.send("Service Not Hosted by RPC Server")
server()