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
import requests

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

url = 'https://www.youtube.com/@%EC%8A%A4%ED%86%A0%EB%A6%AC/videos'

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

#driver = webdriver.Chrome(options=option)
driver.get(url)
driver.implicitly_wait(3)

actions = driver.find_element(By.CSS_SELECTOR,'body')

for i in range(5):
    elem = driver.find_elements(By.CLASS_NAME, 'yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'.replace(' ','.'))
    for el in range(len(elem)):
        thumbnail = elem[el].get_attribute('src')
        title = elem[el].get_attribute('aria-label')
        print(thumbnail)
        try:
            file_name=  f'./youtube_thumbnail/{title}.jpg'
            ss = requests.get(thumbnail, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
        except Exception as e:
            print('에러발생 :',e)
    actions.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    
