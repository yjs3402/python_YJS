minsit = 2
maxsit = 10
people = 6
memo = {}

def solve(remain, sitten):
    key = str([remain, sitten])
    print(key)

    if key in memo:
        return memo[key]
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    cnt = 0
    for sit in range(sitten, maxsit+1):
        cnt += solve(remain - sit, sit)
    memo[key] = cnt
    return cnt

print(solve(people, minsit))