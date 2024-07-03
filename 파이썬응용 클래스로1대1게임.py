import time
import random

class SpecialAttack:
    def __init__(self):
        pass
class NormalAttack:
    def __init__(self, hp, damage, defense):
        pass
    def attack(self):
        return self.damage * self.critical()
    def attacked(self, myname, damage):  
        if(self.miss() == 0):
            print("<<회피<<")
            return
        beforehp = self.hp
        self.hp -= damage * self.defense
        self.printhp(myname, beforehp, damage * self.defense)
    def critical(self):
        if random.randrange(4) == 0:
            print("**치명타**")
            return 2
        else:
            return 1
    def miss(self):
        return random.randrange(5)
    def printhp(self, myname, beforehp, damage):
        print("입힌데미지 {}".format(damage))
        print("{} hp: {} >> {}".format(myname, beforehp, self.hp))

class Player(NormalAttack):
    def __init__(self, hp, damage, defense):
        self.hp = hp
        self.damage = damage
        self.defense = defense / 100
        
def input_status(stat):
    print("{} 스탯".format(stat))
    hp = int(input("hp를 입력 > "))
    damage = int(input("damage를 입력 > "))
    defense = int(input("defense를 입력 > "))
    return hp,damage,defense
#체력, 데미지, 방어력 직접입력
#치명타: 1/4확률로 데미지 두배
#회피율: 1/5확률로 무효
hp, damage, defense = input_status("P1")
P1 = Player(hp,damage, defense)
hp,damage, defense = input_status("P2")
P2 = Player(hp,damage, defense)
while(P1.hp > 0 and P2.hp > 0):
    print()
    print("P1 공격")
    P2.attacked("P2", P1.attack())
    print()
    time.sleep(4)
    print("P2 공격")
    P1.attacked("P1", P2.attack())
    print()
    time.sleep(4)
    print("P1 hp: {}  P2 hp: {}".format(P1.hp, P2.hp))
    print("-----------\n")
    time.sleep(2)
    
if(P1.hp <= 0 and P2.hp <= 0):
    print("DRAW")
elif(P1.hp <= 0):
    print("P2 WIN")
elif(P2.hp <= 0):
    print("P1 WIN")
