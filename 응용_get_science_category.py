import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

nums = ['731', '226', '227']
for i in range(3):
    print(i+1)
    for j in range(5,16):
        print(20240700+j)
        url = 'https://news.naver.com/breakingnews/section/105/{}?date=202407{:02d}'.format(nums[i],j)
        
        site = requests.get(url, headers=headers)
        source_data = site.text

        count = source_data.count('"sa_text_strong">')

        for k in range(count):
            pos1 = source_data.find('"sa_text_strong">')+ len('"sa_text_strong">')
            source_data = source_data[pos1:]

            pos2 = source_data.find('</strong>')
            extract_data = source_data[:pos2]

            pos11 = source_data.find('"sa_text_lede">')+ len('"sa_text_lede">')
            source_data = source_data[pos11:]

            pos22 = source_data.find('</div>')
            extract_data2 = source_data[:pos22]

            source_data = source_data[pos2+1:]
            print(k+1, extract_data)
            print('\t', extract_data2)