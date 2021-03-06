from PyQt4.QtCore import *
from PyChatGUI import *
import socket

## The background thread that acts as the server
class Server(QThread):

    message = pyqtSignal(object)

    def __init__(self, gui):
        QThread.__init__(self)
        self.gui = gui
        self.gui.sendSignal.connect(self.send)
        self.running = True
        self.client = None

    def run(self):
        # Sits and accepts incomming connections and forwards them to the gui
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', 9000))
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.listen(1)
        try:
            while self.running:
                sock, address = self.server.accept()
                self.message.emit(sock)
        finally:
            print 'Closing server...'
            self.server.close()

    def send(self, str_):
        """Convert the message to unicode and send to the client
            str_ : (str) the string to be converted and forwarded
        """

        print 'Sending ' + str_
        if self.client:
          self.client.send(str(str_).encode('utf-8'))

    def close(self):
        self.running = False
        self.server.close()


