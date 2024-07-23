import requests
import time
import os

page_folder = f"/python_YJS/naver_webtoon/{title}"
if not os.path.exists(page_folder):
        os.mkdir(page_folder)