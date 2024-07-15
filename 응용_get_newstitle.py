# requests 모듈을 이용해서
# 네이버 뉴스 메인화면에서 있는 뉴스들 제목 전체 가져오기
import requests

# headers없으면 네이버가 요청차단
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gekco'}

url = 'https://news.naver.com/'             # 원하는 사이트 입력
site = requests.get(url, headers=headers)   # 내용 가져오기
source_data = site.text                     # 인터넷 소스코드를 source_data변수에 저장
count = source_data.count('"cjs_t">')       # 뉴스 제목 개수 가져오기

for i in range(count):                      # 해당 개수만큼 반복
    pos1 = source_data.find('"cjs_t">')+ len('"cjs_t">')    # 뉴스 앞 부분위치 지정
    source_data = source_data[pos1:]                        #해당 위치로 이동

    pos2 = source_data.find('</div>')       # 뉴스 뒷부분 위치 지정
    extract_data = source_data[:pos2]       # 앞부분부터 뒷부분까지 내용 추출해서 저장

    pos11 = source_data.find('"cjs_d">')+ len('"cjs_d">')
    source_data = source_data[pos11:]

    pos22 = source_data.find('</p>')
    extract_data2 = source_data[:pos22]

    source_data = source_data[pos2+1:]      # 다음 뉴스를 찾기위해 뒤부분을 이동시키기
    print(i+1, extract_data)                # 화면에 출력
    print("\t", extract_data2)