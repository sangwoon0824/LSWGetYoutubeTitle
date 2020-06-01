# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UserInfo import userInfo
from GetTitle import getTitle
userInfo = userInfo()
getTitle = getTitle()


#class Ui_Dialog2(QDialog):
#    def __init__(self):
#        super().__init__()
#        self.setupUi(self)
#
#    def setupUi(self, Dialog):
#        Dialog.setObjectName("Dialog")
#        Dialog.resize(200, 50)
#        Dialog.setStyleSheet("background-color:rgb(0,0,0);")
#        self.horizontalSlider = QtWidgets.QSlider(Dialog)
#        self.horizontalSlider.setGeometry(QtCore.QRect(20, 15, 160, 22))
#        self.horizontalSlider.setProperty("value", userInfo.getSound())
#        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
#        self.horizontalSlider.setObjectName("horizontalSlider")
#        self.frame = QtWidgets.QFrame(Dialog)
#        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 50))
#        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#        self.frame.setObjectName("frame")
#        self.frame.raise_()
#        self.horizontalSlider.raise_()
#
#        self.horizontalSlider.valueChanged.connect(self.changeSound)
#
#        self.retranslateUi(Dialog)
#        QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#    def changeSound(self):
#        sound = self.horizontalSlider.value()
#        userInfo.setSound(sound)
#        userInfo.dataSet()
#
#    def retranslateUi(self, Dialog):
#        _translate = QtCore.QCoreApplication.translate
#        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#
class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.id = None
        self.pw = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 139)
        Dialog.setModal(False)
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(20, 25, 251, 40))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet("padding-left:5px;")
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_PW = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_PW.setGeometry(QtCore.QRect(20, 75, 251, 40))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.lineEdit_PW.setFont(font)
        self.lineEdit_PW.setStyleSheet("padding-left:5px;")
        self.lineEdit_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PW.setObjectName("lineEdit_PW")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 40, 75, 60))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.saveFunction)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "유튜브 로그인"))
        self.pushButton.setText(_translate("Dialog", "로그인"))
    
    def saveFunction(self):
        self.id = self.lineEdit_ID.text()
        self.pw = self.lineEdit_PW.text()
        self.close()

class Ui_MainWindow(QMainWindow):
    fontsize = 15
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 80)
        MainWindow.setFixedSize(450, 80)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 450, 100))
        self.frame.setStyleSheet("background-color: rgb(0,0,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(0, -10, 450, 100))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: white; border:0px;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 20))
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.setVisible(False)
        self.action_start = QtWidgets.QAction(MainWindow)
        self.action_start.setObjectName("action_start")
        self.action_login = QtWidgets.QAction(MainWindow)
        self.action_login.setObjectName("action_login")
#        self.action_sound = QtWidgets.QAction(MainWindow)
#        self.action_sound.setObjectName("action_sound")
        self.menu.addAction(self.action_start)
        self.menu.addAction(self.action_login)
#        self.menu.addAction(self.action_sound)
        self.menubar.addAction(self.menu.menuAction())

        self.action_login.triggered.connect(self.loginAction)
        self.action_start.triggered.connect(self.startAction)
#        self.action_sound.triggered.connect(self.soundAction)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "노래 제목 나온당"))
        self.title.setText(_translate("MainWindow", "노래 제목이 나옵니다"))
        self.menu.setTitle(_translate("MainWindow", "메뉴"))
        self.action_start.setText(_translate("MainWindow", "실행"))
        self.action_login.setText(_translate("MainWindow", "유튜브 로그인"))
 #       self.action_sound.setText(_translate("MainWindow", "소리"))

    def loginAction(self):
        ui = Ui_Dialog()
        ui.exec_()
        if ui.id == "" or ui.pw == "":
            userInfo.setID("None")
            userInfo.setPW("None")
            userInfo.setURL(userInfo.getURL())
            userInfo.dataSet()
        else:
            userInfo.setID(ui.id)
            userInfo.setPW(ui.pw)
            userInfo.setURL(userInfo.getURL())
            userInfo.dataSet()

    def startAction(self):
        userID = userInfo.getID()
        userPW = userInfo.getPW()

        getTitle.startWeb()
        self.chageTitle()

    def chageTitle(self):
        t = threading.Timer(1,self.chageTitle)
        t.daemon = True
        try:
            getTitle.findTitle()
            userInfo.setURL(getTitle.getWebURL())
            userInfo.setID(userInfo.getID())
            userInfo.setPW(userInfo.getPW())
            userInfo.dataSet()
            if len(getTitle.title) > 33:
                self.fontsize = (450/len(getTitle.title)) + 1
            else:
                self.fontsize = 15
            font = QtGui.QFont()
            font.setFamily("나눔고딕")
            font.setPointSize(self.fontsize)
            font.setBold(True)
            font.setWeight(75)
            self.title.setFont(font)
            self.title.setText(getTitle.title)
            t.start()
        except Exception as e:
            userInfo.setURL(userInfo.getURL())
            userInfo.setID(userInfo.getID())
            userInfo.setPW(userInfo.getPW())
            userInfo.dataSet()
            t._stop()
            t._delete()
            t.cancel()
            sys.exit()
            
        
        
        


#    def soundAction(self):
#        ui = Ui_Dialog2()
#        ui.exec_()

    def enterEvent(self, e):
        self.menubar.setVisible(True)
        MainWindow.setFixedSize(450, 100)
    
    def leaveEvent(self, e):
        self.menubar.setVisible(False)
        MainWindow.setFixedSize(450, 80)

    def closeEvent(self, a0):
        self.title.setText("종료중...")
        userInfo.setURL(getTitle.getWebURL())
        userInfo.setID(userInfo.getID())
        userInfo.setPW(userInfo.getPW())
        getTitle.theEND()
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
    

