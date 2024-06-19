
try:

    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a ** 2)
except:
    print("정수를 입력하지 않았다.")
else:
    print("예외가 없다")
finally:
    print("일단 어떻게든 끝났다")