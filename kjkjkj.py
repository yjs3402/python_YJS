#pip install selenium webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrom_options = webdriver.ChromeOptions()   #자동으로 다운받은 후 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrom_options)

ID = 'lhj2442'
PW = 'zheld123'
# 지우고 한줄로 써도 사용가능
url = 'https://memeberssl.auction.co.kr/Authenticate/default.aspx?url=http%3A//corners.auction.co.kr/AllKill/AllDay.aspx'
driver.get(url)             # 해당 url로 접속
driver.implicitly_wait(3)   # 인터넷정보 다 다운받을때까지 대기(초)

e = driver.find_element(By.NAME, 'id')
e.clear()
e.send_keys(ID)
e = driver.find_element(By.NAME, 'password')
e.clear()
e.send_keys(PW)
e.send_keys(Keys.ENTER)
driver.implicitly_wait(3)   # 인터넷정보 다 다운받을떄까지 대기(초)

driver.get('http://escrow.auction.co.kr/close/OrderProcessList.aspx?loginType=50')
webpage = driver.page_source

products = driver.find_elements(By.CLASS_NAME, 'product-name')
for i in products: #상품명
    print(i.text)
products = driver.find_elements(By.CLASS_NAME, 'product-order-num')
for i in products: #주문번호
    print(i.text)
products = driver.find_elements(By.CLASS_NAME, 'charge')
for i in products: #상품금액
    print(i.text)