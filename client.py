import socket

def client(inp):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect(("localhost",5500))
    s.send(inp.encode())
    return s.recv(1024)
