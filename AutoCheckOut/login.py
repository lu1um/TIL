#!/usr/bin/env python

from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = 1
SURVEY = 2

MAIN_PATH = __file__ + '\\..\\'

class AutoCheckOut:
    def __init__(self, urltxt, idtxt):
        self.__url = str()
        self.__xpath = str()
        self.__id = str()
        self.__password = str()
        self.__surveyUrl = str()
        self.__surveyXpath = list()
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')

        self.driver.minimize_window()
        self.loadURL(urltxt)
        self.loadID(idtxt)

    def loadURL(self, urltxt, stxt):
        with open(MAIN_PATH + urltxt, 'r') as F:
            self.__url = F.readline()
            self.__url = self.__url.strip('\n')
            self.__xpath = F.readline()
        with open(MAIN_PATH + stxt, 'r') as S:
            pass
            # self.__surveyUrl = S.readline()
            # self.__surveyUrl = self.__surveyUrl.strip('\n')
            # __surveyxpath 반복문으로 저장하기
        # survey #

    def loadID(self, idtxt):
        with open(MAIN_PATH + idtxt, 'r') as F:
            self.__id = F.readline()
            self.__id = self.__id.strip('\n')
            self.__password = F.readline()

    def openURL(self, url=LOGIN):
        if url==LOGIN:
            self.driver.get(self.__url)
            self.driver.implicitly_wait(3)
        elif url==SURVEY:
            pass
        # survey #

    def login(self):
        _id = self.driver.find_element_by_xpath('//*[@id="userId"]')
        _password = self.driver.find_element_by_xpath('//*[@id="userPwd"]')

        _id.send_keys(self.__id)
        _password.send_keys(self.__password)

        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
        self.driver.implicitly_wait(3)
        return True
    
    def checkOut(self):
        self.driver.find_element_by_xpath(self.__xpath).click()

    def thisURL(self): # 지금 이 페이지가 뭔지 알려주는 함수
        pass

    def xPath(self):
        return self.__xpath

    def test(self):
        print(self.__url)
        print(self.CHECKOUT_XPATH)