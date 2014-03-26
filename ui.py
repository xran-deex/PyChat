# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chat_window.ui'
#
# Created: Wed Mar 05 13:47:08 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ChatWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName(_fromUtf8("ChatWindow"))
        ChatWindow.resize(428, 199)
        self.centralwidget = QtGui.QWidget(ChatWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ChatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ChatWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        ChatWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ChatWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ChatWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(ChatWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionConnect = QtGui.QAction(ChatWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        ChatWindow.setWindowTitle(_translate("ChatWindow", "PyChat", None))
        self.sendButton.setText(_translate("ChatWindow", "Send", None))
        self.menuFile.setTitle(_translate("ChatWindow", "File", None))
        self.actionQuit.setText(_translate("ChatWindow", "Quit", None))
        self.actionConnect.setText(_translate("ChatWindow", "Connect", None))

