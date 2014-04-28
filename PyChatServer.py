from PyQt4.QtGui import *
import sys
from ui import Ui_ChatWindow
from Server import *
from Client import *
from PyChatGUI import *
import sys_rc
from PyChatClient import *

class PyChatServer(PyChatClient):

    sendSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        PyChatClient.__init__(self, parent)

        self.clients = []
        self.gui = None

    def showDialog(self):
        """Display the chat dialog"""
        action = self.sender()
        host = self.actions[action]
        ip_address = socket.gethostbyname(host + '.CCPS.WAN')
        self.gui = PyChatGUI(parent=self, socket_=None, ip=ip_address)

    def createActions(self):
        PyChatClient.createActions(self)
        self.createMoreActions()

    def getConnectedPcName(self, socket_):
        """Override this method get the pc name based on the ip address"""
        host = socket_.getpeername()
        ip = socket.gethostbyaddr(host[0])
        address = ip[0].split('.')[0].upper()
        name = self.pc_names[address]
        return name

    def createMoreActions(self):
        """Add all of the PC names and ip address from PCs.txt to the system try menu"""
        self.actions = {}
        self.pc_names = {}
        for line in open('PCs.txt'):
            name, ip_address = line.split(';')
            ip_address = ip_address.strip()
            action = QAction(name, self,
                triggered=self.showDialog)
            self.actions[action] = ip_address
            self.pc_names[ip_address] = name

    def addPCActions(self):
        self.newMenu = QMenu(self)
        self.newMenu.setTitle('PCs')
        self.trayIconMenu.addMenu(self.newMenu)
        for action in self.actions:
            self.newMenu.addAction(action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)
    gui = PyChatServer()
    #gui.show()
    sys.exit(app.exec_())