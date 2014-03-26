import socket

class Server():

    def __init__(self):
        pass

    def serve(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 9000))
        server.listen(1)
        socket_, address = server.accept()
        while True:
            msg = socket_.recv(1024)
            if not msg: break
            print msg
        socket_.close()
        server.close()


    def receive(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(('localhost', 9000))

        inp = raw_input('>> ')
        while inp != 'q':
            server.send(inp)
            msg = server.recv(1024)
            print msg
            inp = raw_input('>> ')


server = Server()
server.receive()