# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portScanner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket
import subprocess
import sys
import threading
from datetime import datetime
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

class Ui_Dialog(object):
    def scannn(self):
        self.progressBar.setValue(0)
        # Clear the screen
        # subprocess.call('notepad', shell=False)

        # Ask for input
        self.remoteServer = self.lineEdit.text()
        self.remoteServerIP = socket.gethostbyname(self.remoteServer)
        self.startPort = self.lineEdit_2.text()
        self.stopPort = self.lineEdit_3.text()
        self.startPort = int(self.startPort)
        self.startPort = self.startPort - 1
        self.stopPort = int(self.stopPort)
        self.stopPort = self.stopPort + 1
        # Print a nice banner with information on which host we are about to scan
        self.listWidget.addItem("___________________________________________________________________________________")
        self.listWidget.addItem("Please wait, scanning remote host {}".format(self.remoteServerIP))
        self.listWidget.addItem("____________________________________________________________________________________")
        self.diff = self.stopPort - self.startPort

        # Check what time the scan started
        self.t1 = datetime.now()

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

        # We also put in some error handling for catching errors
        self.common_ports=[21,22,23,25,80,110,587,3306,8080];
        self.lengthh=9
        self.diff+=9
        self.diff = 100 / self.diff
        self.difff = self.diff
        """if self.checkBox.isChecked == True:
            pass"""

        try:
            
            for self.port in range(self.startPort, self.stopPort):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.result = self.sock.connect_ex((self.remoteServerIP, self.port))
                self.progressBar.setValue(self.diff)
                self.diff += self.difff
                if self.flag == 1:
                    self.listWidget.addItem("Scan stopped")
                    return
                if self.result == 0:
                    self.listWidget.addItem("Port {}: 	 Open".format(self.port))
                    self.comboBox.addItem("{}".format(self.port))
            for self.port in self.common_ports:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.result = self.sock.connect_ex((self.remoteServerIP, self.port))
                self.progressBar.setValue(self.diff)
                self.diff += self.difff
                if self.flag == 1:
                    self.listWidget.addItem("Scan stopped")
                    return
                if self.result == 0:
                    self.listWidget.addItem("Port {}: 	 Open".format(self.port))
                    self.comboBox.addItem("{}".format(self.port))
            self.sock.close()
            self.diff = 100
            self.progressBar.setValue(self.diff)

        except KeyboardInterrupt:
            self.listWidget.addItem("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            self.listWidget.addItem('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            self.listWidget.addItem("Couldn't connect to server")
            sys.exit()

            # Checking the time again
        self.t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        self.total = self.t2 - self.t1

        # Printing the information to screen
        self.listWidget.addItem('Scanning Completed in:{}'.format(self.total))

        
    def scann(self):
        self.progressBar.setValue(0)
        # Clear the screen
        # subprocess.call('notepad', shell=False)

        # Ask for input
        self.remoteServer = self.lineEdit.text()
        self.remoteServerIP = socket.gethostbyname(self.remoteServer)
        self.startPort = self.lineEdit_2.text()
        self.stopPort = self.lineEdit_3.text()
        self.startPort = int(self.startPort)
        self.startPort = self.startPort - 1
        self.stopPort = int(self.stopPort)
        self.stopPort = self.stopPort + 1
        # Print a nice banner with information on which host we are about to scan
        self.listWidget.addItem("___________________________________________________________________________________")
        self.listWidget.addItem("Please wait, scanning remote host {}".format(self.remoteServerIP))
        self.listWidget.addItem("____________________________________________________________________________________")
        self.diff = self.stopPort - self.startPort
        self.diff = 100 / self.diff
        self.difff = self.diff
        # Check what time the scan started
        self.t1 = datetime.now()

        # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

        # We also put in some error handling for catching errors
        # self.common_ports=[21,22,23,25,80,110,587,3306,8080]
        # self.length=common_ports.length()

        """if self.checkBox.isChecked == True:
            pass"""

        try:
            for self.port in range(self.startPort, self.stopPort):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.result = self.sock.connect_ex((self.remoteServerIP, self.port))
                self.progressBar.setValue(self.diff)
                self.diff += self.difff
                if self.flag == 1:
                    self.listWidget.addItem("Scan stopped")
                    return
                if self.result == 0:
                    self.listWidget.addItem("Port {}: 	 Open".format(self.port))
                    self.comboBox.addItem("{}".format(self.port))
            self.sock.close()
            self.diff = 100
            self.progressBar.setValue(self.diff)

        except KeyboardInterrupt:
            self.listWidget.addItem("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            self.listWidget.addItem('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            self.listWidget.addItem("Couldn't connect to server")
            sys.exit()

            # Checking the time again
        self.t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        self.total = self.t2 - self.t1

        # Printing the information to screen
        self.listWidget.addItem('Scanning Completed in:{}'.format(self.total))

    def scan(self):
        self.flag = 0
        self.tt1=None
        if self.checkBox.isChecked() == True:
            self.tt1 = threading.Thread(target=self.scannn)
        else:
            self.tt1 = threading.Thread(target=self.scann)
            
                    
        
        
        
        self.tt1.start()

    def stop(self):

        self.flag = 1
    def send(self):
        ip=self.remoteServerIP
        port = self.comboBox.currentText()
        port=int(port)
        buffer = 1024
        if self.lineEdit_4.text()=="":
            message=bytes.fromhex('5c5350ff')
        message=bytes.fromhex(self.lineEdit_4.text())
        
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(message)
        data=s.recv(buffer)
        s.close()
        self.listWidget_2.addItem("received data:{}".format(data))
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(526, 456)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(72, 70, 101, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 340, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(45, 160, 411, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(50, 380, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 381, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(50, 340, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.scan)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 47, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(50, 130, 101, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 70, 121, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.comboBox = QtGui.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(170, 10, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 390, 111, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.send)
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 60, 451, 261))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 47, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 350, 191, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(80, 350, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Port Scanner", None))
        self.label.setText(_translate("Dialog", "URL", None))
        self.pushButton_2.setText(_translate("Dialog", "Stop", None))
        self.label_3.setText(_translate("Dialog", "Stop Port", None))
        self.pushButton.setText(_translate("Dialog", "Start", None))
        self.label_2.setText(_translate("Dialog", "Start Port", None))
        self.checkBox.setText(_translate("Dialog", "Common Ports", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Scan Open Ports", None))
        self.pushButton_3.setText(_translate("Dialog", "Send Data", None))
        self.label_4.setText(_translate("Dialog", "Ports", None))
        self.label_5.setText(_translate("Dialog", "Byte String", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Attack Open Ports", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

