
try:

    number_input_a = int(input("정수 입력> "))

    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a ** 2)
except:
    print("뭔가 잘못됐어")