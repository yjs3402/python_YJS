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

elem_attri = {
    'y프로필-이름-링크' : ['avatar-link', 'title', 'href'],
    'y프로필-사진' : ['yt-core-image yt-spec-avatar-shape__image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-to-fill yt-core-image--loaded'.replace(' ','.'), 'src'],
    'y카테고리' : ['style-scope yt-chip-cloud-chip-renderer'.replace(' ','.')],
    'y영상' : ['dismissible'],
    'y영상-썸네일' : ['yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded'.replace(' ','.') , 'src'],
    'y영상-제목-링크' : ['video-title-link', 'title', 'href'],
    'y댓글-이름' : ['author-text', 'href'],
    'y댓글-텍스트' : ['yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap'.replace(' ','.')]
}
# 블록 클릭
def click_block(block):
    block.click()
    driver.implicitly_wait(3)
# 크롬 열고 빨대 꽂기
def start_chrome():
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=option)
    return driver
# 사이트 열기
def open_site(driver, url):
    driver.get(url)
    driver.implicitly_wait(3)
    return driver
# 파일에서 오류가나는 특수문자 제거
def del_err_txt(name):
    error_text = ['\\','/',':','*','?','"','<','>','.'] # '.' ..?
    for k in error_text:
        if name.find(k) != -1:
            name = name.replace(k, "")
    return name
# 현재 페이지에서 스크롤 내리기(몇초 기다리기)
def scroll_down(drvier, time):
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    actions.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(time)
# 페이지 맨 아래로 스크롤 내리기(중간중간 몇초 기다리기)
def scroll_to_end(driver, time):
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    before_h = browser.execute_script("return window.scrollY")
    while True:
        actions.send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(time)
        after_h = browser.execute_script("return window.scrollY")
        if after_h == before_h:
            return
        before_h = after_h
# 폴더만들기
def make_folder(address):
    if not os.path.exists(address):
        os.mkdir(address)
# 블럭리스트에서 원하는 속성 추출해서 리스트만들기
def get_attribute_forlist(elements, wanna_del_err_txt, attri):
    attributes = []
    for elem in elements:
        attribute = elem.get_attribute(attri)
        if wanna_del_err_txt == 1:
            attribute = del_err_txt(attribute)
        attributes.append(attribute)
    return attributes
# 이미지 저장하기
def save_picture(address_name, picture):
    try:
        ss = requests.get(picture, headers=headers)
        file = open(address_name, 'wb')
        file.write(ss.content)
        file.close()
    except Exception as e:
        print('에러발생 :',e)
# 원하는 element개수가 로딩될만큼 내리기
def scroll_untill_load(driver, cnt, elem):
    elems = driver.find_elements(By.ID, elem)
    while len(chaneols) < cnt:
        scroll_down(driver, 5)
        elems = driver.find_elements(By.ID, elem)
    return driver
# 유튜브 댓글 저장하기
def save_comments(address):
    names = driver.find_elements(By.ID, elem_attri['y댓글-이름'][0])
    texts = driver.find_elements(By.CLASS_NAME, elem_attri['y댓글-텍스트'][0])[1:]
    for profile in range(len(names)):
        name_url = names[profile].get_attribute(elem_attri['y댓글-이름'][1])
        name = name_url.find('/@')
        name_url = name_url[name + 2:]
        text = texts[profile].text

        comment_txt = open(f'{address}/{profile}_{name_url}.txt', 'w', encoding='UTF-8')
        comment_txt.write(text)
        comment_txt.close()
# 유튜브 원하는 카테고리 들어가기
def youtube_choose_category(driver, text):
    category = driver.find_elements(By.CLASS_NAME, elem_attri['y카테고리'][0])
    for i in range(len(category)):
        if category[i].text == text:
            choosed_category = category[i]
            break
    click_block(choosed_category)
    return driver
# 크롬 열기
driver = start_chrome()

# 유튜브 열기
drive = open_site(driver, 'https://www.youtube.com')

# '최근에 업로드된 동영상'카테고리에 들어가기
driver = youtube_choose_category(driver, '최근에 업로드된 동영상')

chaneol_count = int(input("탐색할 채널 개수 입력> "))
video_count = int(input("채널당 탐색할 영상 개수 입력> "))

chaneol_names = []
chaneol_sites = []
# 원하는개수만큼 채널 블럭을 저장
driver = scroll_untill_load(driver, chaneol_count, elem_attri['y프로필-이름-링크'][0])
# 채널 블럭에서 채널이름, 사이트 추출
chaneols = driver.find_elements(By.ID, elem)
chaneol_names = get_attribute_forlist(chaneols[:chaneol_count], 1, elem_attri['y프로필-이름-링크'][1])
chaneol_sites = get_attribute_forlist(chaneols[:chaneol_count], 0, elem_attri['y프로필-이름-링크'][2])
for i in range(chaneol_count):
    make_folder(f"./youtube_thumbnail/{chaneol_names[i]}") # 각 채널이름으로 폴더생성

# 각 채널 썸네일,댓글 가져오기
for i in range(chaneol_count):
    print(i+1, chaneol_names[i])
    driver = open_site(driver, f'{chaneol_sites[i]}/videos')         # 채널 사이트 접속
    now_file = f"./youtube_thumbnail/{chaneol_names[i]}"

    driver = scroll_untill_load(driver, video_count, elem_attri['y영상'][0])
    
    elems = driver.find_elements(By.CLASS_NAME, elem_attri['y영상-썸네일'][0])[:video_count]
    title_link = driver.find_elements(By.ID, elem_attri['y영상-제목-링크'][0])[:video_count]
    
    thumbnails = get_attribute_forlist(elems, 0, elem_attri['y영상-썸네일'][1])
    titles = get_attribute_forlist(title_link, 1, elem_attri['y영상-제목-링크'][1])
    links = get_attribute_forlist(title_link, 0, elem_attri['y영상-제목-링크'][2])
    for video_num in range(video_count):
        driver = open_site(driver, links[video_num])
        for i in range(2):
            scroll_down(driver, 7)
        time.sleep(10)
        print(video_num+1, titles[video_num])
        make_folder(f"{now_file}/{titles[video_num]}")
        save_picture(f'{now_file}/{titles[video_num]}/{titles[video_num]}.jpg', thumbnails[video_num])
        time.sleep(1)

        save_comments(f"{now_file}/{titles[video_num]}")
    
