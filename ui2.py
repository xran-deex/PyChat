# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chat_window.ui'
#
# Created: Tue Mar  4 16:10:57 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ChatWindow(object):
    def setupUi(self, ChatWindow):
        ChatWindow.setObjectName("ChatWindow")
        ChatWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(ChatWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ChatWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ChatWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ChatWindow)
        self.statusbar.setObjectName("statusbar")
        ChatWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(ChatWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ChatWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatWindow)

    def retranslateUi(self, ChatWindow):
        ChatWindow.setWindowTitle(QtGui.QApplication.translate("ChatWindow", "PyChat", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("ChatWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("ChatWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("ChatWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

