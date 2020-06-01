import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from getDriver import updateDriver
from UserInfo import userInfo


class getTitle(object):  
    savedID = None
    savedPW = None
    title = None
    #driver = None
    userInfo = userInfo()
    lastURL = userInfo.getURL()
    
    
    def startWeb(self):
        try:
            self.driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
        except Exception:
            self.driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
        self.driver.get(self.lastURL)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        userID = self.userInfo.getID()
        userPW = self.userInfo.getPW()
        if userID != "None" and userPW != "None":
            self.driver.implicitly_wait(5)
            self.setIDPW(userID,userPW)
            self.login()
        self.findTitle()
            
        
        

    def findTitle(self):
        self.driver.implicitly_wait(5)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        try:
            getTitle = soup.find('a', {'class' : 'ytp-title-link yt-uix-sessionlink ytp-title-fullerscreen-link'})
            self.title = getTitle.contents[0]
        except AttributeError:
            self.title = "제목 찾는 중..."
        except IndexError:
            self.title = "제목 찾는 중..." 


    def setIDPW(self,_id,_pw):
        self.savedID = _id
        self.savedPW = _pw

        #로그인
    def login(self):
        try:
            self.driver.implicitly_wait(7)
            loginbtn = self.driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a') 
            loginbtn.click()
            self.driver.implicitly_wait(5)
            inputID = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
            inputID.send_keys(self.savedID)
            self.driver.implicitly_wait(3)
            idbtn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
            idbtn.click()
            self.driver.implicitly_wait(10)
            inputPW = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            inputPW.send_keys(self.savedPW)
            self.driver.implicitly_wait(3)
            pwbtn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
            pwbtn.click()
        except:
            self.driver.get('https://www.youtube.com/')

    def theEND(self):
        try:
            if self.driver != None:
                self.driver.quit()
        except Exception as e:
            print(e)


    def getWebURL(self):
        url = self.driver.current_url
        return url

