from roc_sci_pap_package.roc_sci_pap import *

def play():
    score1, score2 = 0, 0
    while last_who_win(score1, score2) == "":
        player1 = input_p1_p2("player1")
        player2 = input_p1_p2("player2")
        result, score1, score2 = who_win(player1, player2, score1, score2)
        print(result, f"\n{score1} : {score2}\n")

    print(last_who_win(score1, score2))

