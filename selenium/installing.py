from selenium import webdriver
import time
import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


url = "http://github.com"

driver.get(url)


driver.save_screenshot("kayitismi.png")



time.sleep(2)

saving =driver.maximize_window()

print(driver.title)

time.sleep(2)


driver.close()