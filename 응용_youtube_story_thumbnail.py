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
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver = webdriver.Chrome(options=option)
driver.get(url)
driver.implicitly_wait(3)

actions = driver.find_element(By.CSS_SELECTOR,'body')
last_height = driver.execute_script("return document.documentElement.scrollHeight")

already_loaded = 0
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    elem = driver.find_elements(By.CLASS_NAME, 'yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'.replace(' ','.'))
    titles = driver.find_elements(By.ID, 'video-title')
    video_url = driver.find_elements(By.CLASS_NAME,'ytp-title-link yt-uix-sessionlink')
    for el in range(len(elem)):
        thumbnail = elem[el].get_attribute('src')
        title = titles[el].get_attribute('aria-label')
        title_end = title.find(' 게시자')
        title = title[:title_end]
        print(thumbnail[already_loaded:])
        print(title[already_loaded:])
        error_text = ['\\','/',':','*','?','"','<','>']
        for k in error_text:
            if title.find(k) != -1:
                title = title.replace(k, '', len(title))
        try:
            file_name=  f'./youtube_thumbnail/{title}.jpg'
            ss = requests.get(thumbnail, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
        except Exception as e:
            print('에러발생 :',e)
    already_loaded = len(elem)
    if new_height == last_height:
        break
    last_height = new_height
    
