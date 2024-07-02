import time
import random
class player:
    def __init__(self, hp, damage, defense):
        self.__hp = hp
        self.damage = damage
        self.defense = defense
    def attack(self, target):
        beforehp = target.hp
        target.hp -= self.damage * self.miss() * self.critical()
        print("hp: {} >> {}".format(beforehp, target.hp))
    def critical(self):
        if random.randrange(4) == 0:
            print("*치명타*")
            return 2
        else
            return 1
    def miss(self):
        misspercent = random.randrange(3)
        if misspercent == 0:
            print("<<회피!<<")
        return misspercent
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value
def input_status():
    hp = int(input("hp를 입력 > "))
    damage = int(input("damage를 입력 > "))
    defense = int(input("defense를 입력 > "))
    return hp,damage,defense
#체력, 데미지, 방어력 직접입력
#치명타: 1/4확률로 데미지 두배
#회피율: 1/3
hp, damage, defense = input_status()
P1 = player(hp,damage, defense)
hp,damage = input_status()
P2 = player(hp,damage, defense)
while(P1.hp > 0 and P2.hp > 0):
    print("P1 공격")
    P1.attack(P2)
    print("P2 공격")
    P2.attack(P1)
    print("P1의 hp: {} P2의 hp: {}".format(P1.hp, P2.hp))
    print()
    time.sleep(1)
    
if(P1.hp <= 0 and P2.hp <= 0):
    print("DRAW")
elif(P1.hp <= 0):
    print("P2 WIN")
elif(P2.hp <= 0):
    print("P1 WIN")
