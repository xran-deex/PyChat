from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_dialog import *
from Client import *
import os, socket

class PyChatGUI(QDialog, Ui_Dialog):

    send_message_signal = pyqtSignal(str)

    def __init__(self, parent=None, socket_=None, ip=None):
            QDialog.__init__(self)
        # try:
            if not socket_:
                print ip
                self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_.connect((ip, 9000))
            else:
                self.socket_ = socket_

            self.client = Client(self, self.socket_)
            self.client.receive_message_signal.connect(self.receive_message)
            self.client.start()

            self.parent = parent
            self.parent.trayIcon.messageClicked.connect(self.showDialog)
            self.setupUi(self)
            self.setVisible(True)
            self.sendButton.clicked.connect(self.send_message)

    def showDialog(self):
        self.setVisible(True)

    def send_message(self):
        self.textBrowser.append('me: ' + self.lineEdit.text())
        self.send_message_signal.emit(self.lineEdit.text())
        self.lineEdit.setText('')
        self.lineEdit.setFocus()

    def receive_message(self, msg):
        try:
            name = self.parent.get_connected_pc_name(self.socket_)
        except Exception as e:
            print e
            print 'Closing sockets...'
            self.socket_.close()
            self.parent.server.close()
            return

        if not self.isVisible():
            self.parent.trayIcon.showMessage('New message', 'You have a new message from ' + name)
        self.textBrowser.append(name + ': ' + unicode(msg))
        self.lineEdit.setText('')
        self.lineEdit.setFocus()

    def closeEvent(self, event):
        self.setVisible(False)
        self.socket_.close()
        event.ignore()