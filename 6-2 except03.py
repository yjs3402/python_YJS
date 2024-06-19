
list_number = [52, 273, 32, 72, 100]


try:
    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해라()
except ValueError as exception:
    print("정수를 입력하라고!")
    print("exception:",exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗ㅅ어났다!")
    print("exception:",exception)