from time import sleep
import random
        
class Object:
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.__hp = hp
        self.__damage = damage
        self.__defense = 1 - defense / 100
    def attack(self):
        return self.__damage
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

class SpecialAttack(Object):
    def __init__(self):
        self.noattack = 0
    def spc_attack(self):
        return self.damage * 7

class Player(SpecialAttack):
    def __init__(self, name, hp, damage, defense):
        super().__init__(name, hp, damage, defense)
    def attacktype(self, att_type, target):
        if att_type == "x":
            print("공격을 하지않았습니다")
            self.noattack += 1
        elif att_type == "o":
            target.attacked(target.name, self.attack())
        elif att_type == "spc":
            if self.noattack >= 4:
                target.spc_attacked(self.spc_attack())
        else:
            print("o, x, spc 중에 입력하시오")
            input_att_type(self, target)

    def miss(self):
        rand = random.randrange(10)
        if rand == 0:
            print("<<회피<<")
        return (rand == 0)
    def critical(self):
        rand = random.randrange(10)
        if rand == 0:
            print("**치명타**")
        return (rand == 0)
    def attacked(self, myname, damage):
        if(self.miss()):
            return
        
        if(self.critical()):
            iscritical = 2
        else:
            iscritical = 1
        beforehp = self.hp
        totaldamage = damage * self.defense * iscritical
        self.hp -= totaldamage
        self.printhp(myname, beforehp, totaldamage, "o")
    def spc_attacked(self, myname, spc_damage):
        beforehp = self.hp
        self.hp -= spc_damage
        self.printhp(myname, beforehp, spc_damage, "spc")
    def printhp(self, myname, beforehp, damage, att_type):
        if att_type == "o":
            print("입힌데미지 {}".format(damage))
        else:
            print("궁극기데미지 {}".format(damage))
        print("{} hp: {} >> {}".format(myname, beforehp, self.hp))


        
def input_status(stat):
    print("{} 스탯".format(stat))
    name = input("name을 입력 > ")
    hp = int(input("hp를 입력 > "))
    damage = int(input("damage를 입력 > "))
    defense = int(input("defense를 입력 > "))
    return name, hp, damage, defense
def input_att_type(cls1, cls2):
    att_type = input("공격 유형(o, x, spc) > ")
    cls1.attacktype(att_type, cls2)
# 체력, 데미지, 방어력 직접입력
# 치명타: 1/10확률로 데미지 두배
# 회피율: 1/10확률로 무효
# 공격4번 안하면 스킬(데미지 7배)
name, hp, damage, defense = input_status("P1")
P1 = Player(name, hp, damage, defense)
name, hp,damage, defense = input_status("P2")
P2 = Player(hp,damage, defense)
while(P1.hp > 0 and P2.hp > 0):
    print()
    print("P1 공격")
    input_att_type(P1, P2)

    sleep(0)
    print()
    print("P2 공격")
    input_att_type(P2, P1)

    sleep(0)
    print()
    print("P1 hp: {}  P2 hp: {}".format(P1.hp, P2.hp))
    print("-------------------------")
    sleep(0)
    
if(P1.hp <= 0 and P2.hp <= 0):
    print("DRAW")
elif(P1.hp <= 0):
    print("P2 WIN")
elif(P2.hp <= 0):
    print("P1 WIN")
