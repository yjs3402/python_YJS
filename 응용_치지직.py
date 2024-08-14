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
# 크롬 열고 빨대 꽂기
def start_chrome():
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=option)
    return driver, headers
# 사이트 열기
def open_site(driver, url):
    driver.get(url)
    driver.implicitly_wait(3)
    return driver
# 블록 클릭
def click_block(block):
    block.click()
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
def scroll_down(drvier, sec):
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    actions.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(sec)
# 페이지 맨 아래로 스크롤 내리기(중간중간 몇초 기다리기)
def scroll_to_end(driver, sec):
    actions = driver.find_element(By.CSS_SELECTOR, 'body')
    before_h = browser.execute_script("return window.scrollY")
    while True:
        actions.send_keys(Keys.PAGE_DOWN)
        driver.implicitly_wait(sec)
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
def save_picture(address_name, picture, headers):
    try:
        ss = requests.get(picture, headers=headers)
        file = open(address_name, 'wb')
        file.write(ss.content)
        file.close()
    except Exception as e:
        print('에러발생 :',e)
# 원하는 element개수가 로딩될만큼 내리기
def scroll_untill_load(driver, cnt, elem):
    elems = renewal_find_elements(driver, elem)
    while len(elems) < cnt:
        scroll_down(driver, 5)
        elems = renewal_find_elements(driver, elem)
    return driver
# 유튜브 댓글 저장하기
def save_comments(address):
    names = renewal_find_elements(driver, elem_attri['y댓글-이름'][0])
    texts = renewal_find_elements(driver, elem_attri['y댓글-텍스트'][0])[1:]
    for profile in range(len(names)):
        name_url = names[profile].get_attribute(elem_attri['y댓글-이름'][1])
        name = name_url.find('/@')
        name_url = name_url[name + 2:]
        text = texts[profile].text

        comment_txt = open(f'{address}/{profile}_{name_url}.txt', 'w', encoding='UTF-8')
        comment_txt.write(text)
        comment_txt.close()
# 원하는 카테고리 들어가기
def click_category(driver, elem, text):
    category = renewal_find_elements(driver, elem)
    for i in category:
        if i.text == text:
            choosed_category = i
            break
    driver = click_block(choosed_category)
    return driver
# element 종류 자동으로 찾기
def renewal_find_elements(drive, value, start=0, end=-1):
    elements = []
    By_list = [By.CLASS_NAME, By.ID, By.NAME, By.TAG_NAME]
    for i in By_list:
        try:
            elem = drive.find_elements(i, value)
        except:
            elem = []
        else:
            elements = elem
            break
    if end == 1:
        return elements[0]
    return elements[start:end]

def renewal_find_element(drive, value):
    element = []
    By_list = [By.CLASS_NAME, By.ID, By.NAME, By.TAG_NAME]
    for i in By_list:
        try:
            elem = drive.find_element(i, value)
        except:
            elem = []
        else:
            element = elem
            break
    return element


# 크롬 열기
driver, headers = start_chrome()

# 치지직 열기
driver = open_site(driver, 'https://chzzk.naver.com')

# 광고가 있으면 닫기
if renewal_find_element(driver, 'loungehome_event_popup_main__S7h8c'):
    del_block = renewal_find_element(driver, 'loungehome_event_popup_button_close__ftfLQ')
    driver = click_block(del_block)

# 전체방송 카테고리 들어가기
driver = click_category(driver, 'header_text__SNWKj', '인기\n클립')

channel_count = int(input("탐색할 채널 개수 입력> "))
video_count = int(input("탐색할 영상 개수 입력> "))
scroll_untill_load(driver, video_count, 'navigation_component_item__iMPOI')
videos = driver.find_elements(By.CLASS_NAME, 'navigation_component_item__iMPOI')
print(len(videos))
videos = videos[:video_count]
links = []
names = []
images = []
for video in videos:
    link_block = video.find_element(By.TAG_NAME, 'a')
    link = link_block.get_attribute('href')
    
    name = video.find_element(By.CLASS_NAME, 'clip_card_title__Pc2jc').text
    name = del_err_txt(name)
    
    image_block = video.find_element(By.CLASS_NAME, 'clip_card_container__aoMWB')
    image = image_block.get_attribute('style')
    image_begin = image.find('background-image: url("') + len('background-image: url("')
    image_end = image.find('");"')
    image = image[image_begin : image_end]
    
    links.append(link)
    names.append(name)
    images.append(image)

for link in range(len(links)):
    driver = open_site(driver, links[link])
    save_picture(f'./치지직_클립/{link + 1} {names[link]}.jpg', images[link], headers)
    
