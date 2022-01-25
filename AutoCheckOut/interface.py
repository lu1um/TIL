#!/usr/env/bin python

from threading import Timer
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtGui import QFont

import login

SEC_DELAY = 5

class MainWindow(QMainWindow):
    def __init__(self, urldir, iddir, surveytxt, dftxt):
        super(MainWindow, self).__init__()
        self.__loginTime = 0
        self.__loginMin = 0

        self.__initUI(dftxt)
        self.__timerOn()
        try:
            self.aco = login.AutoCheckOut(urldir, iddir, surveytxt)
        except:
            self.pleaseTxt()
            exit()
        self.__loadIDPW()
    
    def __initUI(self, dftxt):
        self.setGeometry(0, 0, 800, 800)  # x, y, w, h
        self.setWindowTitle('AutoCheckOut')
        self.status_bar = self.statusBar()
        # text box
        self.txtbox_id = QLineEdit(self)
        self.txtbox_id.move(100, 150)
        self.txtbox_id.resize(250, 30)
        self.txtbox_pw = QLineEdit(self)
        self.txtbox_pw.move(100, 250)
        self.txtbox_pw.resize(250, 30)
        self.txtbox_sv = QLineEdit(self)
        self.txtbox_sv.move(100, 350)
        self.txtbox_sv.resize(250, 30)
        self.txtbox_sv.setText(dftxt)
        # text box label
        self.id = QLabel(self)
        makeLabel(self.id, 100, 120, 12, text='ID')
        self.pw = QLabel(self)
        makeLabel(self.pw, 100, 220, 12, text='Password')
        self.sv = QLabel(self)
        makeLabel(self.sv, 100, 320, 12, text='설문조사 주소')
        # push button
        btn_act = QPushButton('&Activate', self)
        btn_act.clicked.connect(self.__activate)
        btn_act.setStyleSheet('background-color: green; color: white')
        btn_act.move(100, 400)
        # radio button
        rbt_login = QRadioButton('출첵', self)
        rbt_login.setChecked(True)
        rbt_login.move(100, 50)
        rbt_none = QRadioButton('로그인만', self)
        rbt_none.move(200, 50)
        self.actMode = QButtonGroup()
        self.actMode.addButton(rbt_login, 0)
        self.actMode.addButton(rbt_none, 1)

        rbt_in = QRadioButton('출석', self)
        rbt_in.move(100, 75)
        rbt_out = QRadioButton('퇴실', self)
        rbt_out.move(200, 75)
        rbt_out.setChecked(True)
        self.isOut = QButtonGroup()
        self.isOut.addButton(rbt_in, 0)
        self.isOut.addButton(rbt_out, 1)
        # timer display
        self.ampm = QLabel(self)
        makeLabel(self.ampm, 370, 150, 20)
        self.ampm_hour = QLabel(self)
        makeLabel(self.ampm_hour, 450, 150, 20, align=Qt.AlignRight)
        self.ampm_min = QLabel(self)
        makeLabel(self.ampm_min, 520, 150, 20, align=Qt.AlignRight)
        self.ampm_sec = QLabel(self)
        makeLabel(self.ampm_sec, 590, 150, 20, align=Qt.AlignRight)
        # activate flag display
        self.act = QLabel(self)
        self.act.move(370, 400)
        self.act.setText('...')
        self.act.resize(300, 50)

        self.show()
    
    def __loadIDPW(self):
        id, pw = self.aco.getIDPW()
        self.txtbox_id.setText(id)
        self.txtbox_pw.setText(pw)
    
    def __writeIDPW(self):
        self.aco.receiveID(self.txtbox_id.text(), self.txtbox_pw.text())
    
    def pleaseTxt(self):
        QMessageBox.about(self, 'ACO', '같은 폴더 내 필요한 파일\nURL.txt\nSURVEY.txt\n')

    def survey(self):

        pass

    def __timerOn(self):
        t = time.time()
        kor = time.localtime(t)
        if kor.tm_hour>12:
            korhour = kor.tm_hour-12
            ampm = '오후'
        else:
            korhour = kor.tm_hour
            ampm = '오전'

        self.ampm.setText(f'{ampm}')
        self.ampm_hour.setText(f'{korhour}시')
        self.ampm_min.setText(f'{kor.tm_min}분')
        self.ampm_sec.setText(f'{kor.tm_sec}초')

        timer = Timer(1, self.__timerOn)
        timer.start()
        if self.__loginTime:
            self.__startChrome(kor)
        
    def __activate(self):
        if self.actMode.checkedId():    # 로그인만이 선택되었을때
            self.act.setText('로그인중...')
            self.act.setStyleSheet('Color : black')
            self.__loginTime = 1
        else:
            if self.isOut.checkedId():  # 저녁 6시
                self.act.setText('저녁 6시를 기다리는 중')
                self.act.setStyleSheet('Color : green')
                self.__loginTime = 18
                self.__loginMin = 0
            else:
                self.act.setText('아침 8시 30분을 기다리는 중')
                self.act.setStyleSheet('Color : green')
                self.__loginTime = 8
                self.__loginMin = 30
        self.__writeIDPW()

    def __startChrome(self, kor):
        if self.actMode.checkedId():
            self.__loginTime = 0
            self.aco.maximize()
            self.aco.openURL(login.LOGIN)
            self.aco.login()
            self.act.setText('로그인 완료!')
        elif kor.tm_hour >= self.__loginTime and kor.tm_min >= self.__loginMin and kor.tm_sec >= SEC_DELAY:
            self.__loginTime = 0
            self.aco.maximize()
            self.aco.openURL(login.LOGIN)
            if self.aco.login():
                self.aco.checkOut()
            self.act.setText('출석체크 완료!')

    
    def __loadID(self):
        pass
    

def makeLabel(label, x, y, fontsize=20, fontcolor='black', align=Qt.AlignLeft, text=''):
    label.move(x, y)
    label.setFont(QFont('Arial', fontsize))
    label.setStyleSheet(f'Color: {fontcolor}')
    label.setAlignment = align
    label.setText(text)