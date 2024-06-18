# 랜덤한 숫자를 만들기 위해 가져옵니다.
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))
