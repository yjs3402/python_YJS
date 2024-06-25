def input_p1_p2(name):
    while True:
        try:
            p = int(input(f"{name} > "))
        except ValueError as exception:
            print("정수를 입력")
        else:
            if 1<=p<=3:
                break
            print("1, 2, 3 중에 입력")
    return p

def who_win(p1, p2, s1, s2):
    if p1==p2:
        return ("DRAW", s1, s2)
    elif (((p1-p2+3)%3)==1):
        return ("player1 WIN", s1+1, s2)
    else:
        return ("player2 WIN", s1, s2+1)

def last_who_win(s1, s2):
    if s1 == 3:
        return "Finally player1 WIN!!"
    elif s2 == 3:
        return "Finally player2 WIN!!"
    else:
        return ""

def play():
    score1, score2 = 0, 0
    while last_who_win(score1, score2) == "":
        player1 = input_p1_p2("player1")
        player2 = input_p1_p2("player2")
        result, score1, score2 = who_win(player1, player2, score1, score2)
        print(result, f"\n{score1} : {score2}\n")

    print(last_who_win(score1, score2))

