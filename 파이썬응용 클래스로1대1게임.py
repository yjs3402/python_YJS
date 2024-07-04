from time import sleep
import random
        
class object:
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.__hp = hp
        self.__damage = damage
        self.__defense = 1 - defense / 100
    def attack(self):
        return self.__damage * self.critical()
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value
    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value
    @property
    def defense(self):
        return self.__defense
    @defense.setter
    def defense(self, value):
        self.__defense = value

class SpecialAttack(object):
    def __init__(self):
        self.noattack = 0
    def ultimate(self):


class Player(object, SpecialAttack):
    def __init__(self, name, hp, damage, defense):
        super().__init__(name, hp, damage, defense)
    def attacktype(self, att_type, target)
        if att_type = "X":
            print("공격을 하지않았습니다")
            self.noattack += 1
        elif att_type = "O":
            target.attacked(target.name, P1.attack())
        elif att_type = "SPC":
            if self.noattack >= 4:

    def miss(self):
        return random.randrange(10)
    def critical(self):
        if random.randrange(4) == 0:
            print("**치명타**")
            return 2
        else:
            return 1
    def spc_attacked(self):

    def attacked(self, myname, damage):
        if(self.miss() == 0):
            print("<<회피<<")
            return
        beforehp = self.hp
        self.hp -= damage * self.defense
        self.printhp(myname, beforehp, damage * self.defense)
    def printhp(self, myname, beforehp, damage):
        print("입힌데미지 {}".format(damage))   
        print("{} hp: {} >> {}".format(myname, beforehp, self.hp))


        
def input_status(stat):
    print("{} 스탯".format(stat))
    name = int(input("name을 입력 > "))
    hp = int(input("hp를 입력 > "))
    damage = int(input("damage를 입력 > "))
    defense = int(input("defense를 입력 > "))
    return hp,damage,defense
# 체력, 데미지, 방어력 직접입력
# 치명타: 1/10확률로 데미지 두배
# 회피율: 1/10확률로 무효
# 공격4번 안하면 스킬
name, hp, damage, defense = input_status("P1")
P1 = Player(hp,damage, defense)
name, hp,damage, defense = input_status("P2")
P2 = Player(hp,damage, defense)
while(P1.hp > 0 and P2.hp > 0):
    print()
    print("P1 공격")
    att_type = input("공격 유형(O, X, SPC) > ")
    P1.attacktype(att_type, P2)

    print()
    sleep(0)
    print("P2 공격")
    P1.attacked("P1", P2.attack())

    print()
    sleep(0)
    print("P1 hp: {}  P2 hp: {}".format(P1.hp, P2.hp))
    print("-------------------------")
    sleep(0)
    
if(P1.hp <= 0 and P2.hp <= 0):
    print("DRAW")
elif(P1.hp <= 0):
    print("P2 WIN")
elif(P2.hp <= 0):
    print("P1 WIN")
