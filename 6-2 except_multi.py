
list_number = [52, 273, 32, 72, 100]


try:
    number_input = int(input("정수 입력> "))

    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력하라고!")
except IndexError:
    print("리스트의 인덱스를 벗ㅅ어났다!")