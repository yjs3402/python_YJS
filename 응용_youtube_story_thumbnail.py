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
import os

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

url = 'https://www.youtube.com/@%EC%8A%A4%ED%86%A0%EB%A6%AC/videos'

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver = webdriver.Chrome(options=option)
driver.get(url)
driver.implicitly_wait(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

already_loaded = 0
titles = []
links = []
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    elem = driver.find_elements(By.CLASS_NAME, 'yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'.replace(' ','.'))
    titles_links = driver.find_elements(By.ID, 'video-title-link')
    for el in range(already_loaded,len(elem)):
        thumbnail = elem[el].get_attribute('src')
        title = titles_links[el].get_attribute('title')
        link = titles_links[el].get_attribute('href')
        error_text = ['\\','/',':','*','?','"','<','>','.']
        for k in error_text:
            if title.find(k) != -1:
                title = title.replace(k, "", len(title))
        titles.append(title)
        links.append(link)
        print(thumbnail)
        print(title)
        print(link)
        page_folder = f"./youtube_thumbnail/{title}"
        if not os.path.exists(page_folder):
            os.mkdir(page_folder)
        
        try:
            file_name=  f'./youtube_thumbnail/{title}/{title}.jpg'
            ss = requests.get(thumbnail, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
        except Exception as e:
            print('에러발생 :',e)
        time.sleep(1)
    already_loaded = len(elem)
    if new_height == last_height:
        break
    last_height = new_height
    
for li in range(len(links)):
    driver.get(links[li])
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)
    names = driver.find_elements(By.ID, 'author-text')
    texts = driver.find_elements(By.CLASS_NAME,'yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap')[1:]
    for profile in range(len(names)):
        name_url = names[profile].get_attribute('href')
        name = name_url.find('/@')
        name_url = name_url[name + 2:]
        text = texts[profile].text

        comment_txt = open(f"./youtube_thumbnail/{titles[li]}/{name_url}.txt",'w')
        comment_txt.write(text)
        comment_txt.close()
        
        
