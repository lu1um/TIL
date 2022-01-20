#!/usr/env/bin python

from threading import Timer
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap, QPainter, QPen, QFont, QImage

import login

class MainWindow(QMainWindow):
    def __init__(self, urldir, iddir):
        super(MainWindow, self).__init__()

        self.__initUI()
        self.aco = login.AutoCheckOut(urldir, iddir)
    
    def __initUI(self):
        self.setGeometry(0, 0, 800, 800)  # x, y, w, h
        self.setWindowTitle('AutoCheckOut')
        self.status_bar = self.statusBar()
        # text box
        self.txtbox = QLineEdit(self)
        self.txtbox.move(100, 150)
        self.txtbox.resize(250, 30)
        self.txtbox.setText('아산/배방읍/자택')
        # push button
        btn_act = QPushButton('&Activate', self)
        btn_act.clicked.connect(self.__activate)
        btn_act.setStyleSheet('background-color: green; color: white')
        btn_act.move(100, 200)
        # radio button
        rbt_login = QRadioButton('login', self)
        rbt_login.setChecked(True)
        rbt_login.move(100, 50)
        rbt_none = QRadioButton('none', self)
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

        self.show()

    def timerOn(self):
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

        timer = Timer(1, self.timerOn)
        timer.start()
        
    def __activate(self):
        _xpath = self.aco.xPath()
        self.aco.openURL(_xpath)
        if self.aco.login():
            self.aco.checkOut()
        

    
    def __readButtonGroup(self):
        want = self.actMode.checkedId()
