p1 = int(input("player1 > "))
p2 = int(input("player2 > "))

if p1==p2:
    print("DRAW")
elif (((p1-p2+3)%3)==1):
    print("player1 WIN")
else:
    print("player2 WIN")

'''
if player1==player2:
        print("DRAW")
elif (player1=="가위" and player2=="바위") or \
   (player1=="바위" and player2=="보") or \
   (player1=="보" and player2=="가위"):
        print("player2 WIN")
else:
    print("player1 WIN")
'''

