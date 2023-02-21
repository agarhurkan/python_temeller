from githubUserInfo import username , password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys






class Github:
    def __init__(self, username,password) :
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(options=options)

        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        username = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")
        password = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
        
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]").click()

    def loadFollowers(self):
        items = self.browser.find_elements(By.XPATH,"/html/body/div[1]/div[5]/main/div[2]/div/div[2]/turbo-frame/div/div/div[2]/a")  
        for i in items :
            i=i.text 
            self.followers.append(i)

    def getFollowers(self):
        self.browser.get("https://github.com/serkanalc?tab=followers")
        time.sleep(2)

        self.loadFollowers()

        while True :
            links = self.browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME,"a")
            
            if len(links) == 1 :
                if links [0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else :
                    break
            else:
                for link in links :
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)

                        self.loadFollowers()   
                    else:
                        continue
            

github = Github(username,password)

time.sleep(2)

github.signIn()
github.getFollowers()
yieldsort =  1
for i in github.followers :
    print(yieldsort,":",i)
    yieldsort+=1