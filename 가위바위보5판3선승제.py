def ro_si_pa(p1, p2):
    if p1==p2:
        print("DRAW")
    elif (((p1-p2+3)%3)==1):
        print("player1 WIN")
        win["p1"]+=1
    else:
        print("player2 WIN")
        win["p2"]+=1

win = {
    "p1": 0,
    "p2": 0
}

verses = 0
while True:
    player1 = int(input("player1 >"))
    player2 = int(input("player2 >"))
    ro_si_pa(player1, player2)
    print(win)
    verses+=1
    if verses == 5:
        print("DRAW!!")
        break
    elif win["p1"]==3:
        print("player1 WIN!!")
        break
    elif win["p2"]==3:
        print("player2 WIN!!")
        break
    
        
