# 시작하기전 아래 모듈 설치(cmd창 통해서 입력)
# pip install selenium subprocess pyperclip webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
url = 'http://naver.com'

user_id = '08michael'
user_pw = '121yjskaka'

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

#driver = webdriver.Chrome(options=option)
driver.get(url)
driver.implicitly_wait(3)

elem = driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
elem.click()
driver.implicitly_wait(3)


elem_id = driver.find_element(By.ID,'id')
elem_id.click()
pyperclip.copy(user_id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

elem_pw = driver.find_element(By.ID,'pw')
elem_pw.click()
pyperclip.copy(user_pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element(By.ID, 'log.login').click()

input()