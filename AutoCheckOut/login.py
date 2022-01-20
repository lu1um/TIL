#!/usr/bin/env python

from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_PATH = __file__ + '\\..\\'

class AutoCheckOut:
    def __init__(self, urltxt, idtxt):
        self.__url = str()
        self.__xpath = str()
        self.__id = str()
        self.__password = str()
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')

        self.driver.minimize_window()
        self.loadURL(urltxt)
        self.loadID(idtxt)

    def loadURL(self, urltxt):
        with open(MAIN_PATH + urltxt, 'r') as F:
            self.__url = F.readline()
            self.__url = self.__url.strip('\n')
            self.__xpath = F.readline()

    def loadID(self, idtxt):
        with open(MAIN_PATH + idtxt, 'r') as F:
            self.__id = F.readline()
            self.__id = self.__id.strip('\n')
            self.__password = F.readline()

    def openURL(self, waitForElement):
        self.driver.get(self.__url)
        self.driver.implicitly_wait(3)
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, waitForElement)))

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

        # 설문참여 위에서 5번째, 보충수업 신청설문
        # //*[@id="wrap"]/form/div/div[2]/div/div/ul/li[5]/div/div[3]/a