import datetime

today = datetime.datetime.now()
cnt = 0
now_to_newyear = []
while True:
    before = today - datetime.timedelta(days=cnt)
    MonthDay = int(before.strftime("%m%d"))
    now_to_newyear.append(before)
    if MonthDay==101:
        break
    else:
        cnt+=1

newyear_to_now = list(reversed(now_to_newyear))
for mmdd in newyear_to_now:
    print(mmdd.strftime("%m{} %d{}").format("월","일"))
