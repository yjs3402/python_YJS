import requests
import time
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

for i in range(204,215):
    url = f'https://www.youtube.com/@스토리/videos?app=desktop'
    site = requests.get(url,headers=headers)
    source_data = site.text
    title_start = source_data.find('<meta property="og:title" content="') + len('<meta property="og:title" content="')
    source_data = source_data[title_start:]
    title_end = source_data.find(' - ')
    fulltitle_end = source_data.find('">')
    title = source_data[:title_end]
    fulltitle = source_data[:fulltitle_end]
    print(title)
    print(fulltitle)
    page_folder = f"./python_YJS/naver_webtoon/{title}"
    if not os.path.exists(page_folder):
        os.mkdir(page_folder)

    page_folder = f"./python_YJS/naver_webtoon/{title}/{fulltitle}"
    if not os.path.exists(page_folder):
        os.mkdir(page_folder)

    
    content_start = source_data.find('#FFFFFF">') + len('#FFFFFF">')
    source_data = source_data[content_start:]
    content_end = source_data.find('</div>')
    source_data = source_data[:content_end]
    count = source_data.count('<img src="')
    for j in range(count):
        image_start = source_data.find('<img src="') + len('<img src="')
        source_data = source_data[image_start:]

        image_end = source_data.find('"')
        image = source_data[:image_end]
        print(i, '-', j+1, image)
        
        try:
            file_name=  f'./python_YJS/naver_webtoon/{title}/{fulltitle}/{fulltitle}{j+1}{image[-4:]}'
            ss = requests.get(image, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)
            file.close()

        except Exception as e:
            print('에러발생 :',e)
        time.sleep(0.5)