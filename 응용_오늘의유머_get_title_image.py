import requests
import time
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}
for i in range(100):
    page_folder = f"C:/Users/c403/Documents/GitHub/python_YJS/todayhumor/todayhumer_page{str(i+1)}"
    if not os.path.exists(page_folder):
        os.mkdir(page_folder)
    url = f'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page={str(i+1)}'
    site = requests.get(url,headers=headers)
    source_data = site.text

    content_count = source_data.count('"subject"><a href="')
    for j in range(content_count):
        url_start = source_data.find('"subject"><a href="') + len('"subject"><a href="')
        source_data = source_data[url_start:]

        url_end = source_data.find('" target="_top">')
        article_url = source_data[:url_end]

        title_start = source_data.find('" target="_top">') + len('" target="_top">')
        source_data = source_data[title_start:]

        title_end = source_data.find('</a>')
        title = source_data[:title_end]
        content_url = 'https://www.todayhumor.co.kr' + article_url

        print('페이지',i+1,'-',j+1, title)
        print('\t' + content_url)

        error_text = ['\\','/',':','*','?','"','<','>']
        for k in error_text:
            if title.find(k) != -1:
                title = title.replace(k, '', len(title))
                
        content_folder = page_folder + '/' + title
        if not os.path.exists(content_folder):
            os.mkdir(content_folder)

        content_site =requests.get(content_url,headers=headers)
        content_data = content_site.text
        content_start = content_data.find('<div class="viewContent">') + len('<div class="viewContent">')
        content_end = content_data.find('</div><!--viewContent-->')
        content_data = content_data[content_start:content_end]
        count = content_data.count('<img src="')
        print('\t이미지')
        for k in range(count):
            image_start = content_data.find('<img src="') + len('<img src="')
            content_data = content_data[image_start:]

            image_end = content_data.find('"')
            image = content_data[:image_end]

            try:
                file_name=  f'./todayhumor/todayhumer_page{str(i+1)}/{title}/{title}{k+1}.{image[-3:]}'
                ss = requests.get(image, headers=headers)
                file = open(file_name, 'wb')
                file.write(ss.content)
                file.close()

            except Exception as e:
                print('에러발생 :',e)

            print('\t', image)
        time.sleep(2)
