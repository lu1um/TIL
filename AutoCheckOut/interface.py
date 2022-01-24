#!/usr/env/bin python

from threading import Timer
import time
import schedule

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap, QPainter, QPen, QFont, QImage

import login

SEC_DELAY = 5

class MainWindow(QMainWindow):
    def __init__(self, urldir, iddir, dftxt):
        super(MainWindow, self).__init__()
        self.__loginTime = 0

        self.__initUI(dftxt)
        self.__timerOn()
        self.aco = login.AutoCheckOut(urldir, iddir)
    
    def __initUI(self, dftxt):
        self.setGeometry(0, 0, 800, 800)  # x, y, w, h
        self.setWindowTitle('AutoCheckOut')
        self.status_bar = self.statusBar()
        # text box
        self.txtbox = QLineEdit(self)
        self.txtbox.move(100, 150)
        self.txtbox.resize(250, 30)
        self.txtbox.setText(dftxt)
        # push button
        btn_act = QPushButton('&Activate', self)
        btn_act.clicked.connect(self.__activate)
        btn_act.setStyleSheet('background-color: green; color: white')
        btn_act.move(100, 200)
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
        self.setStyleSheet('QLabel{font-size: 20pt;}')
        self.ampm = QLabel(self)
        self.ampm.move(400, 148)
        self.ampm_hour = QLabel(self)
        self.ampm_hour.move(420, 150)
        self.ampm_hour.setAlignment(Qt.AlignRight)
        self.test = QLabel(self)
        self.ampm_min = QLabel(self)
        self.ampm_min.move(490, 150)
        self.ampm_min.setAlignment(Qt.AlignRight)
        self.ampm_sec = QLabel(self)
        self.ampm_sec.move(560, 150)
        self.ampm_sec.setAlignment(Qt.AlignRight)
        # activate flag display
        self.act = QLabel(self)
        self.act.move(350, 200)
        self.act.setText('...')
        self.act.resize(300, 50)

        self.show()

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
        if self.isOut.checkedId():  # 저녁 6시
            self.act.setText('저녁 6시를 기다리는 중')
            self.act.setStyleSheet('Color : green')
            self.__loginTime = 18

    def __startChrome(self, kor):
        if kor.tm_hour >= self.__loginTime and kor.tm_min >= 0 and kor.tm_sec >= SEC_DELAY:
            self.__loginTime = 0
            _xpath = self.aco.xPath()
            self.aco.openURL(_xpath)
            if self.aco.login():
                self.aco.checkOut()
            self.act.setText('출석체크 완료!')
    
    def __readButtonGroup(self):
        want = self.actMode.checkedId()
    

