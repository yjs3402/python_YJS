def Hanoitop(plate, start, end, assist):
    if plate == 1:
        print("{}탑 -> {}탑".format(start,end))

    if plate >= 2:
        Hanoitop(plate-1, start, assist, end)
        print("{}탑 -> {}탑".format(start,end))
        Hanoitop(plate-1, assist, end, start)

plate_num = int(input("원판의 개수를 입력하세요: "))
Hanoitop(plate_num, "A", "B", "C")
print("이동 횟수는 {}회입니다.".format(2 ** plate_num - 1))