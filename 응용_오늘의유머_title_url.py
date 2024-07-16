import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url,headers=headers)
source_data = site.text

count = source_data.count('"subject"><a href="')
for i in range(count):
    url_start = source_data.find('"subject"><a href="') + len('"subject"><a href="')
    source_data = source_data[url_start:]

    url_end = source_data.find('" target="_top">')
    article_url = source_data[:url_end]

    title_start = source_data.find('" target="_top">') + len('" target="_top">')
    source_data = source_data[title_start:]

    title_end = source_data.find('</a>')
    title = source_data[:title_end]
    print(title)
    print('https://www.todayhumor.co.kr' + article_url)