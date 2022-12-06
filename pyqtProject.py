# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
import serial
#Serial 통신 설정
PORT = 'COM9'
BaudRate = 9600
ARD= serial.Serial(PORT,BaudRate)
time_DATA=0

#pyqt를 사용하여 타이머 구현 및 Serial 통신을 사용하여 아두이노의 센서값 3개를 받아와서 출력하는 Project 입니다.
#qt designer을 통해 대략적인 틀을 제작 하였습니다.
#또한 받아온 센서값을 통해 1번째 센서값이 10 이상의 값이 출력되면 이미지가 test2.png로 바뀌게 구현해보았습니다. 

def Decode(A):#아두이노 Original DATA  LIST 형태로 변환
    A = A.decode()
    A = str(A)
    A=A.rstrip('\r\n')
    A=A.split(",")
    return A
def Ardread():#아두이노 Original DATA 받아오기
        if ARD.readable():
            LINE = ARD.readline()
            code=Decode(LINE) 
            return code
        else : 
            print("Error from _Ardread_")
class Ui_Dialog(object):

    def __init__(self,Dialog):#아두이노 동작,갱신주기 설정 & RUN
        self.setupUi(Dialog)
        self.timer = QTimer()
        self.time = QTimer()
        self.timer.start(500)#0.5Sec 마다 값 refresh
        self.time.start(1000)#타이머 시간 계산
        self.timer.timeout.connect(self.update)
        self.time.timeout.connect(self.timeCal)
        print(self.time)

    def update(self):#변환된 DATA 실시간 출력
        arddata=Ardread()
        self.data.setText(arddata[0])
        self.data2.setText(arddata[1])
        self.data3.setText(arddata[2])
        if int(arddata[0])>10:
            self.image.setPixmap(QtGui.QPixmap("image1.png"))#DATA가 >10일시 image1출력
        else:
            self.image.setPixmap(QtGui.QPixmap("image0.png"))


    def timeCal(self):#시간 계산및 출력
        global time_DATA
        time_DATA+=1
        self.label.setText("{0:^2} : {1:^2} : {2:^2}".format(time_DATA//3600,(time_DATA%3600)//60,time_DATA%60))

    def setupUi(self,Dialog):#UI 초기 설정,배치
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 330, 171, 71))
        self.textEdit.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setTabStopWidth(40)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName("textEdit")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(0, 50, 251, 331))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("image.png"))#기본 이미지 출력
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 350, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 410, 171, 71))
        self.textEdit_2.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setTabStopWidth(40)
        self.textEdit_2.setAcceptRichText(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 420, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")   
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(250, 190, 131, 131))
        self.textEdit_5.setSizeIncrement(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setTabStopWidth(40)
        self.textEdit_5.setAcceptRichText(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(253, 190, 231, 151))
        font = QtGui.QFont()
        font.setFamily("휴먼편지체")
        font.setPointSize(13)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.data = QtWidgets.QLabel(Dialog)
        self.data.setGeometry(QtCore.QRect(320, 150, 231, 151))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(False)
        font.setPointSize(18)
        self.data.setFont(font)
        self.data.setObjectName("data")
        self.data2 = QtWidgets.QLabel(Dialog)
        self.data2.setGeometry(QtCore.QRect(320, 190, 231, 151))
        self.data2.setFont(font)
        self.data2.setObjectName("data2")
        self.data3 = QtWidgets.QLabel(Dialog)
        self.data3.setGeometry(QtCore.QRect(320, 230, 231, 151))
        self.data3.setFont(font)
        self.data3.setObjectName("data3")
        self.textEdit.raise_()
        self.image.raise_()
        self.label.raise_()
        self.textEdit_5.raise_()
        self.label_4.raise_()
        self.data.raise_()
        self.data2.raise_()
        self.data3.raise_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.textEdit.setPlaceholderText(_translate("Dialog", "   사용시간"))
            self.label.setText(_translate("Dialog", "NULL:NULL:NULL"))
            self.textEdit_5.setPlaceholderText(_translate("Dialog", "Sensor Data"))
            self.label_4.setText("SENS1 |\n\nSENS2 |\n\nSENS3 |")
            self.data.setText("0")
            self.data2.setText("0")
            self.data3.setText("0")

import sys
import time
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog(Dialog)
ui.setupUi(Dialog)
Dialog.update()
if __name__ == "__main__":
    import sys#
    Dialog.show()
    sys.exit(app.exec_())#프로그램 시작
   



