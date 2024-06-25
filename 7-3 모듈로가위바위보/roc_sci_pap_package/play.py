import roc_sci_pap as rsp

def play():
    score1, score2 = 0, 0
    while rsp.last_who_win(score1, score2) == "":
        player1 = rsp.input_p1_p2("player1")
        player2 = rsp.input_p1_p2("player2")
        result, score1, score2 = rsp.who_win(player1, player2, score1, score2)
        print(result, f"\n{score1} : {score2}\n")

    print(rsp.last_who_win(score1, score2))
