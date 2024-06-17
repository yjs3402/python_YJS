import random

number = []
b=2
for i in range(b):
    number.append(random.randint(1,100000000000000000000000))

for num in number:
    cnt=0
    for i in str(num):
        cnt+=1
    print(cnt)
