class Token(object):
    pass

class Exec(Token):
    pass

class Battle(Exec):
    pass

class Push(Exec):
    pass

class Move(Exec):
    pass

class Sniper(Exec):
    pass

class Granate(Exec):
    pass

class Bomb(Exec):
    pass

'''
class BoardToken(Token):

class Unit(BoardToken):

class Module(BoardToken):

'''


class TokenFactory(object):
    def create_exec_tokens(self,Army):
        if Army.name=="Moloch":
            exectokens = {Battle:4, Move:1, Push:5, Bomb:1}
        elif Army.name=="Borgo":
            exectokens = {Battle:6, Move:4, Granate:1}
        elif Army.name=="Outpost":
            exectokens = {Battle:6, Move:7, Sniper:1}        
        elif Army.name=="Hegemony":
            exectokens = {Battle:5, Move:3, Push:2, Sniper:1}
            
        return [Battle() for i in range(exectokens[Battle])]

class Army(object):
    def __init__(self, name):
        self.name=name

class UnitBuilder(object): 

    def __init__(self):
        self.name = None
        self.initiative = None
        self.hp = None
        self.attacks = [None for i in range(6)]

    def set_hp(self, hp):
        self.hp = hp

    def set_initiative(self, initiative):
        self.initiative = initiative

    def add_attack(self,is_range,multi):
        pass

class Unit(object):
    def __init__(self):
        pass

class Attack(object):
    def __init__(self, is_range, n):
        self.is_range = is_range
        self.n = n
