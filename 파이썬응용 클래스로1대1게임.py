from time import sleep
import random
        
class Stat:
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

class SpecialAttack(Stat):
    def __init__(self):
        self.noattack = 0
    def spc_attack(self):    
        return self.damage * 5
    
# 체력, 데미지, 방어력 직접입력
# 치명타: 1/10확률로 데미지 두배
# 회피율: 1/10확률로 무효
# 공격4번 안하면 스킬(데미지 5배, 방어력 영향x)

class Player(SpecialAttack):
    def __init__(self, name, hp, damage, defense):
        Stat.__init__(self, name, hp, damage, defense)
        SpecialAttack.__init__(self)
    def attacktype(self, att_type, target):
        if att_type == "x":
            print("공격을 하지않았습니다")
            self.noattack += 1
        elif att_type == "o":
            target.attacked(target.name, self.attack())
        elif att_type == "spc":
            if self.noattack >= 4:
                target.spc_attacked(target.name, self.spc_attack())
                self.noattack -= 4
            else:
                print("궁게이지가 4 미만입니다. 현재 궁게이지:", self.noattack)
                input_att_type(self, target)
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

class monster(Stat):
    def __init__(self, difficulty):
        if difficulty == "easy":
            self.difficulty_easy()
        if difficulty == "normal":
            self.difficulty_normal()
        if difficulty == "hard":
            self.difficulty_hard()
        if difficulty == "veryhard":
            self.difficulty_veryhard()
    def difficulty_easy(self):
        pass
    def difficulty_normal(self):
        pass
    def difficulty_hard(self):
        pass
    def difficulty_veryhard(self):
        pass
    def mon_soldier_knife(self, hp, damage):
        pass
    def mon_soldier_gun(self,):
        pass
    def mon_tanker(self):
        pass
    def mon_tanker_metal(self):
        pass
    def mon_witch(self):
        pass
    def mon_boss(self):
        pass

def input_battletype():
    while(1):
        battletype = input("대결 방식을 선택하시오 \nm : 몬스터와 대결\nu : 유저와 1대1\np : 파티 구성하여 대결\n 입력> ")
        if battletype == 'm':
            fight_with_monster()
            break
        elif battletype == 'u':
            fight_with_user()
            break
        elif battletype == 'p':
            fight_with_party()
            break
        else:
            print(" (m, u, p)중에 입력")

def fight_with_monster():
    while(1):
        difficulty = input("난이도 선택(easy, normal, hard, veryhard) > ")
        if difficulty == "easy":
            monster(difficulty)
        else:
            print(" (m, u, p)중에 입력")

def fight_with_party():
    pass

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
def fight_with_user():
    name, hp, damage, defense = input_status("P1")
    P1 = Player(name, hp, damage, defense)
    name, hp, damage, defense = input_status("P2")
    P2 = Player(name, hp, damage, defense)
    while(P1.hp > 0 and P2.hp > 0):
        print()
        print(P1.name, "공격")
        input_att_type(P1, P2)

        sleep(0)
        print()
        print(P2.name, "공격")
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