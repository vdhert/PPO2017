from abc import ABCMeta, abstractmethod

class Token(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def create(self): pass

class Exec(Token):

    def __init__(self):
        Token.__init__(self)

    @staticmethod
    def create(army):
#        if army.name == "Moloch":
#            exectokens = {Battle: 4, Move: 1, Push: 5, Bomb:1}
#        elif army.name == "Borgo":
#            exectokens = {Battle: 6, Move: 4, Granate: 1}
#        elif army.name == "Outpost":
#            exectokens = {Battle: 6, Move: 7, Sniper: 1}
#        elif army.name == "Hegemony":
#            exectokens = {Battle: 5, Move: 3, Push: 2, Sniper: 1}
        return [Battle() for i in range(army.exectokens[Battle])]

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
    def __init__(self):
        Token.__init__(self)

    @classmethod
    def create(cls, army):
        tokens = getattr(army, cls.__name__.lower())
        for el in tokens:
            for key in el:
                key(cls.builder, el[key])

class Module(BoardToken):
    pass


class Army(object):

    def __init__(self, name):
        self.name=name

class Moloch(Army):
    exectokens = {Battle: 4, Move: 1, Push: 5, Bomb:1}
    unit = [{UnitBuilder.set_name: "Lowca", UnitBuilder.set_initiative: 3, UnitBuilder.add_attack: [(False, 1, x) for x in (0, 1, 3, 5)]},
            {UnitBuilder.set_name: "Klaun", UnitBuilder.set_initiative: 2, UnitBuilder.add_attack: [(False, 1, 0),(False, 1, 5)], UnitBuilder.set_hp: 2}]


class UnitBuilder(object): 

    def __init__(self):
        self.name = None
        self.initiative = None
        self.hp = 1
        self.attacks = []
        self.init_segs = 1
        
    def set_name(self, name):
        self.name = name

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

    builder = UnitBuilder()

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









