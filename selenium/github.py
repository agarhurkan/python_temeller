from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url="http://github.com"

driver.get(url)
time.sleep(1)


searchInput = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
 
time.sleep(2)


sonuc = driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/main/div/div[3]/div/ul/li/div[2]/div[1]/div[1]")

print(len(sonuc))

for element in sonuc:
    print(element.text)


driver.close()

