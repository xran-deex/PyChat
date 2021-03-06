from PyQt4.QtGui import *
import sys
from ui import Ui_ChatWindow
from Server import *
from Client import *
from PyChatGUI import *
import sys_rc


class PyChat(QMainWindow, Ui_ChatWindow):

    sendSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.setupUi(self)

        self.clients = []
        if sys.platform == 'darwin':
           self.menubar.setNativeMenuBar(False)

        self.server = Server(self)
        self.server.message.connect(self.receiveMessage)
        self.server.start()
        
        self.createActions()
        self.createTrayIcon()

        self.sendButton.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)
        self.actionQuit.triggered.connect(qApp.quit)

        self.trayIcon.setIcon(QIcon(':images/trash.svg'))
        self.trayIcon.show()


    def showDialog(self):
        action = self.sender()
        host = self.actions[action]
        ip_address = socket.gethostbyname(host + '.CCPS.WAN')
        self.gui = PyChatGUI(parent=self, socket_=None, ip=ip_address)


    def receiveMessage(self, msg):
        PyChatGUI(self, msg)

    def connectToServer(self):
        self.client = Client(self)
        self.client.start()
        self.sendSignal.connect(self.client.send_message)
        self.client.message.connect(self.receiveMessage)

    def send_message(self):
        self.textBrowser.append(self.lineEdit.text())
        self.sendSignal.emit(self.lineEdit.text())
        self.lineEdit.setText('')
        self.lineEdit.setFocus()

    def createActions(self):

        self.connectAction = QAction("&Send Message", self,
                triggered=self.showDialog)

        self.quitAction = QAction("&Quit", self,
                triggered=qApp.quit)

        self.createMoreActions()

    def createMoreActions(self):
        self.actions = {}
        for line in open('PCs.txt'):
            name, ip_address = line.split(';')
            action = QAction(name, self,
                triggered=self.showDialog)
            self.actions[action] = ip_address.strip()

    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.connectAction)
        for action in self.actions:
            self.trayIconMenu.addAction(action)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def setVisible(self, visible):
        self.connectAction.setEnabled(self.isMaximized() or not visible)
        super(PyChat, self).setVisible(visible)

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            QMessageBox.information(self, "Systray",
                    "The program will keep running in the system tray. To "
                    "terminate the program, choose <b>Quit</b> in the "
                    "context menu of the system tray entry.")
            # self.hide()
            # self.client.running = False
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)
    gui = PyChat()
    #gui.show()
    sys.exit(app.exec_())