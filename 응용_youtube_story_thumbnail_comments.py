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

def click_block(block):
    block.click()
    driver.implicitly_wait(3)
def start_chrome():
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return option
def open_site(driver, url):
    driver.get(url)
    driver.implicitly_wait(3)
def delete_error_text(name):
    error_text = ['\\','/',':','*','?','"','<','>','.']
    for k in error_text:
        if name.find(k) != -1:
            name = name.replace(k, "")
    return name
            
def youtube_choose_category(driver, text):
    category = driver.find_elements(By.CLASS_NAME, 'style-scope yt-chip-cloud-chip-renderer'.replace(' ','.'))
    for i in range(len(category)):
        if category[i].text == text:
            choosed_category = category[i]
            break
    return choosed_category

option = start_chrome()

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver = webdriver.Chrome(options=option)

open_site(driver, 'https://www.youtube.com')

recently_uploaded = youtube_choose_category(driver, '최근에 업로드된 동영상')
click_block(recently_uploaded)

chaneol_count = int(input("탐색할 채널 개수 입력> "))
video_count = int(input("채널당 탐색할 영상 개수 입력> "))

chaneols = driver.find_elements(By.ID, 'avatar-link')
chaneol_names = []
chaneol_sites = []
while len(chaneols) < chaneol_count:
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    actions.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    chaneols = driver.find_elements(By.ID, 'avatar-link')
for i in range(chaneol_count):
    chaneol_name = chaneols[i].get_attribute('title')
    chaneol_name = delete_error_text(chaneol_name)
    chaneol_site = chaneols[i].get_attribute('href')
    
    chaneol_names.append(chaneol_name)
    chaneol_sites.append(chaneol_site)
    
    page_folder = f"./youtube_thumbnail/{chaneol_name}"
    if not os.path.exists(page_folder):
        os.mkdir(page_folder)

for i in range(chaneol_count):
    url = f'{chaneol_sites[i]}/videos'
    now_file = f"./youtube_thumbnail/{chaneol_names[i]}"
    driver.get(url)
    driver.implicitly_wait(3)

    titles = []
    links = []
    video = driver.find_elements(By.ID, 'dismissible')
    while len(video) < video_count:
        actions = driver.find_element(By.CSS_SELECTOR, 'body')
        actions.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        video = driver.find_elements(By.ID, 'dismissible')

    for video_num in range(video_count):
        print(video_num+1, end=' ')
        elem = video[video_num].find_element(By.CLASS_NAME, 'yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'.replace(' ','.'))
        title_link = video[video_num].find_element(By.ID, 'video-title-link')
        thumbnail = elem.get_attribute('src')
        title = title_link.get_attribute('title')
        title = delete_error_text(title)
        link = title_link.get_attribute('href')
        titles.append(title)
        links.append(link)
        print(title)
        page_folder = f"{now_file}/{title}"
        if not os.path.exists(page_folder):
            os.mkdir(page_folder)
        try:
            file_name=  f'{now_file}/{title}/{title}.jpg'
            ss = requests.get(thumbnail, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()
        except Exception as e:
            print('에러발생 :',e)
        time.sleep(1)
            
    for li in range(len(links)):
        driver.get(links[li])
        driver.implicitly_wait(5)
        for i in range(2):
            actions = driver.find_element(By.CSS_SELECTOR, 'body')
            actions.send_keys(Keys.PAGE_DOWN)
            time.sleep(7)
        time.sleep(10)
        names = driver.find_elements(By.ID, 'author-text')
        texts = driver.find_elements(By.CLASS_NAME,'yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap')[1:]
        for profile in range(len(names)):
            name_url = names[profile].get_attribute('href')
            name = name_url.find('/@')
            name_url = name_url[name + 2:]
            text = texts[profile].text

            comment_txt = open(f"{now_file}/{titles[li]}/{profile}{name_url}.txt", 'w', encoding='UTF-8')
            comment_txt.write(text)
            comment_txt.close()
    
