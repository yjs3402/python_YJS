from time import sleep
import random
''' 몬스터와 결투 추가하기
    무기 추가하기
    기존 대결(1ㄷ1) 개선하기
    파티 대결 추가하기
'''
class Stat:
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.__starthp = hp
        self.__nowhp = hp
        self.__damage = damage
        self.__defense = 1 - defense / 100
        self.__location = 0
        self.__attackrange = 0
    def move(self, direction):
        if direction == 'a':
            self.__location -= 1
            return
        elif direction == 'd':
            self.__location += 1
            return
        elif direction == 's' or direction == 'w':
            return 
    def attack(self):
        return self.__damage
    def can_attack(self, cls1, cls2):
        return (cls2.location - cls1.location) <= self.__attackrange
    def printhp(self, damage, att_type):
        if att_type == "o":
            print("입은데미지 {}".format(damage))
        elif att_type == "spc":
            print("궁극기데미지 {}".format(damage))
        print(self.name, "{}/{}".format(self.nowhp,self.starthp))
        hprate = int((self.nowhp / self.starthp) * 10)
        print("█ " * hprate, "⎕ " * (10 - hprate))
    @property
    def nowhp(self):
        return self.__nowhp
    @nowhp.setter
    def nowhp(self, value):
        self.__nowhp = value
    @property
    def starthp(self):
        return self.__starthp
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
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, value):
        self.__location = value
    @property
    def attackrange(self):
        return self.__attackrange
    @attackrange.setter
    def attackrange(self, value):
        self.__attackrange = value

class SpecialAttack(Stat):
    def __init__(self):
        self.noattack = 0
    def spc_attack(self):    
        return self.damage * 5

# 한턴에 한번움직이고 한번 공격
# 체력, 데미지, 방어력 직접입력
# 치명타: 1/10확률로 데미지 두배
# 회피율: 1/10확률로 무효
# 공격4번 안하면 스킬(데미지 5배, 방어력 영향x)

class Player(SpecialAttack):
    def __init__(self, name, hp, damage, defense):
        Stat.__init__(self, name, hp, damage, defense)
        SpecialAttack.__init__(self)
    def input_move(self):
        dir = input("")
        self.move(dir)
    def attacktype(self, att_type, target_type, target):
        if target_type == 'p':
            if att_type == "x":
                print("공격을 하지않았습니다")
                self.noattack += 1
            elif att_type == "o":
                target.attacked(self.attack())
            elif att_type == "spc":
                if self.noattack >= 4:
                    target.spc_attacked(self.spc_attack())
                    self.noattack -= 4
                else:
                    print("궁게이지가 4 미만입니다. 현재 궁게이지:", self.noattack)
                    input_att_type(self, target_type, target)
            else:
                print("o, x, spc 중에 입력하시오")
                input_att_type(self, target_type, target)
        elif target_type == 'm':
            if att_type == "x":
                print("공격을 하지않았습니다")
                self.noattack += 1
            elif att_type == "o":
                target.attacked(self.attack())
            elif att_type == "spc":
                if self.noattack >= 4:
                    target.spc_attacked(self.spc_attack())
                    self.noattack -= 4
                else:
                    print("궁게이지가 4 미만입니다. 현재 궁게이지:", self.noattack)
                    input_att_type(self, target_type, target)
            else:
                print("o, x, spc 중에 입력하시오")
                input_att_type(self, target_type, target)
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
    def attacked(self, damage):
        if(self.miss()):
            return
        
        if(self.critical()):
            iscritical = 2
        else:
            iscritical = 1
        self.nowhp -= damage * self.defense * iscritical
        self.printhp(totaldamage, "o")
    def spc_attacked(self, spc_damage):
        self.nowhp -= spc_damage
        self.printhp(spc_damage, "spc")
    def attacked_by_mon(self, damage):
        self.nowhp -= damage * self.defense
        self.printhp(damage, "o")

class Monster(Stat):
    def __init__(self, name, hp, damage, defense, mon_type):
        super().__init__(name, hp, damage, defense)
        self.__mon_type = mon_type
        if self.__mon_type == "SK":
            self.mon_soldier_knife()
        elif self.__mon_type == "SG":
            self.mon_soldier_gun()
        elif self.__mon_type == "T":
            self.mon_tanker()
        elif self.__mon_type == "TM":
            self.mon_tanker_metal()
        elif self.__mon_type == "W":
            self.mon_witch()
        elif self.__mon_type == "B":
            self.mon_boss()
    def move(self):
        super().move('a')
    def can_move(self, front_loc):
        return front_loc < self.location - 1
    def attacked(self, damage, att_type, isTM):
        if isTM == 'x':
            self.nowhp -= damage
            printhp(damage, att_type)
        elif isTM =='o':
            attacked_TM()
    def attacked_TM(self):
        self.nowhp -= 1
        print(self.name, "{}/{}".format(self.nowhp,self.starthp))
        print("█ " * self.nowhp, "⎕ " * (self.starthp - self.nowhp))
    def mon_soldier_knife(self):
        self.attackrange = 1
    def mon_soldier_gun(self):
        self.attackrange = 3
    def mon_tanker(self):
        self.attackrange = 1
    def mon_tanker_metal(self):
        self.attackrange = 1
    def mon_witch(self):
        self.attackrange = 4
    def mon_boss(self):
        self.attackrange = 1000000
    @property
    def mon_type(self):
        return self.__mon_type
apperance = {
    Player : "▶",
    Monster : {
        "SK": "△",
        "SG": "▽",
        "T" : "○",
        "TM": "◎",
        "W" : "◈",
        "BS": "▣"
    }
}
def show_figure(field_size, namelist):
    for i in range(len(namelist)):
        n = namelist[i]
        if i == 0:
            print("▢" * (n.location - 1), end = '')
        else:
            print("▢" * (n.location - namelist[i-1].location - 1), end = '')
        if type(n) == Player:
            print(apperance[type(n)], end = '')
        else:
            print(apperance[type(n)][n.mon_type], end = '')
    print("▢" * (field_size - namelist[len(namelist)-1].location))


def set_location(namelist, *locat):
    for i in range(len(namelist)):
        namelist[i].location = locat[i]
def turn_act(player, monlist, whose_turn):
    if whose_turn == 'p':
        player.input_move()
        input_att_type(player, 'm', monlist)
    elif whose_turn =='m':
        totaldamage = 0
        for i in range(len(monlist)):
            front_loc = monlist[i-1].location
            if i == 0:
                front_loc = 0
            if monlist[i].can_attack(player, monlist[i]):
                totaldamage += monlist[i].damage
            elif monlist[i].can_move(front_loc):
                    monlist[i].move()
        player.attacked_by_mon(totaldamage)


def input_att_type(cls1, target_type, cls2):
    if target_type == 'p':
        att_type = input("공격 유형(o, x, spc) > ")
        cls1.attacktype(att_type, target_type, cls2)
    elif target_type == 'm':
        att_type = input("공격 유형(o, x, spc) > ")
        if att_type == 'o':
            if not(cls1.can_attack(cls1, cls2[0])):
                print("공격할 수 있는 타겟이 없슴다")
                input_att_type(cls1, target_type, cls2)
            else:
                can_attack_list = []
                can_attack_namelist = []
                for i in cls2:
                    if cls1.can_attack(cls1, i):
                        can_attack_list.append(i)
                        can_attack_namelist.append(i.name)
                choose_target = input("타겟 설정", can_attack_namelist, "입력 > ")
        elif att_type == 'spc':
            for i in cls2:
                if i.mon_type != "TM":
                    cls1.attacktype(att_type, target_type, i)
                else:
                    pass
        else:
            pass
            

def input_battletype():
    while True:
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
            print(" 다시 입력")

def fight_with_monster():
    while True:
        difficulty = input("난이도 선택(tutorial, easy, normal, hard, veryhard) > ")
        if difficulty == "tutorial":
            fight_with_monster_tutorial()
            break
        elif difficulty == "easy":
            pass
            break
        elif difficulty == "normal":
            pass
            break
        elif difficulty == "hard":
            pass
            break
        elif difficulty == "veryhard":
            pass
            break
        else:
            print(" 다시 입력")

def fight_with_monster_tutorial():
    name = input("name을 입력 > ")
    player = Player(name, 1000000, 1000000, 0)
    SK = Monster("SK", 100, 100, 0, "SK")
    monlist = [SK]
    alllist = [player] + monlist
    print("WAVE 1")
    print("검사: 거리가 1일때 타격하는 기본 몹이다(제일 만만하다!)")
    field_size = 6
    set_location(alllist, 2,5)
    show_figure(field_size, alllist)
    for i in range(3):
        sleep(0.7)
        turn_act(player, monlist, 'm')
        show_figure(field_size, alllist)
    sleep(1)
    print("공격받았다. 반격!")
    turn_act(player, monlist, 'p')




def fight_with_party():
    pass

def input_player_status(stat):
    print("{} 스탯".format(stat))
    name = input("name을 입력 > ")
    hp = int(input("hp를 입력 > "))
    damage = int(input("damage를 입력 > "))
    defense = int(input("defense를 입력 > "))
    return name, hp, damage, defense

def fight_with_user():
    name, hp, damage, defense = input_player_status("P1")
    P1 = Player(name, hp, damage, defense)
    name, hp, damage, defense = input_player_status("P2")
    P2 = Player(name, hp, damage, defense)
    while(P1.nowhp > 0 and P2.nowhp > 0):
        print()
        print(P1.name, "공격")
        input_att_type(P1, "p", P2)

        sleep(2)
        print()
        print(P2.name, "공격")
        input_att_type(P2, "p", P1)

        sleep(2)
        print()
        print("P1 : {}  P2 : {}".format(P1.nowhp, P2.nowhp))
        print("-------------------------")
        sleep(2)
        
    if(P1.nowhp <= 0 and P2.nowhp <= 0):
        print("DRAW")
    elif(P1.nowhp <= 0):
        print("P2 WIN")
    elif(P2.nowhp <= 0):
        print("P1 WIN")

input_battletype()