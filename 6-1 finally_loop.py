print("프로그램이 시작됨")

while True:
    try:
        print("try 구문이 실행됨")
        break
        print("try 구문의 break 키워드 뒤다")
    except:
        print("except 구문이 실행됨")
    finally:
        print("finally 구문이 실행됨")
    print("while 반복문의 마지막 줄이다.")
print("프로그램이 종료.")