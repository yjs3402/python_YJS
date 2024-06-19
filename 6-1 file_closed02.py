try:
    file = open("info.txt", "w")

    예외.발생해라()

    file.close()
except:
    print("오류가 발생했다.")
    
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed)