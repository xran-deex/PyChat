from PyQt4.QtCore import *
import socket

class Client(QThread):

    receive_message_signal = pyqtSignal(object)

    def __init__(self, gui, socket_=None):
        QThread.__init__(self)
        print 'creating client...'
        self.socket_ = socket_
        self.gui = gui
        self.running = True
        self.gui.send_message_signal.connect(self.send)

    def run(self):
        while self.running:
            val = self.socket_.recv(1024)
            if not val: break
            print 'Received: ' + val
            self.receive_message_signal.emit(val)
        self.socket_.close()

    def send(self, msg):
        self.socket_.send(msg)