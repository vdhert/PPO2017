class Token(object):
    pass

class Exec(Token):

    def execute(self):
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


class BoardToken(Token):
    pass


class Module(BoardToken):
    pass


class TokenFactory(object):
    def create_exec_tokens(self, army):
        if army.name == "Moloch":
            exectokens = {Battle:4, Move:1, Push:5, Bomb:1}
        elif army.name == "Borgo":
            exectokens = {Battle:6, Move:4, Granate:1}
        elif army.name == "Outpost":
            exectokens = {Battle:6, Move:7, Sniper:1}        
        elif army.name == "Hegemony":
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
        self.attacks = []
        self.init_segs = 1

    def set_hp(self, hp):
        self.hp = hp

    def set_initiative(self, initiative):
        self.initiative = initiative

    def add_attack(self, is_range, multi, dir):
        self.attacks.append((is_range, multi, dir))
        
    def set_init_segs(self, n = 1):
        self.init_segs = n

    def build(self):
        return Unit(self.hp, self.initiative, [(c, Attack(a, b)) for a, b, c in self.attacks])


class Unit(BoardToken):

    def __init__(self, hp, init, attacks, init_segs = 1):
        self.hp = hp
        self.initiative = init
        self.attacks = {}
        self.init_segs = init_segs
        for i in attacks:
            self.attacks.setdefault(i[0], []).append(i[1])


class Attack(object):

    def __init__(self, is_range, n):
        self.is_range = is_range
        self.n = n
