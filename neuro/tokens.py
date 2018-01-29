from abc import ABCMeta, abstractmethod


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

    def add_attack(self, is_range, multi, dir_):
        self.attacks.append((is_range, multi, dir_))
        
    def set_init_segs(self, n = 1):
        self.init_segs = n

    def reset_attacks(self):
        self.attacks = []

    def build(self):
        print 'build()', self.attacks
        return Unit(self.name, self.hp, self.initiative, [(c, Attack(a, b)) for a, b, c in self.attacks])


class Token(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def create(self): pass
        
    def __repr__(self):
        return "<{0}>".format(type(self).__name__)


class Exec(Token):

    def __init__(self):
        Token.__init__(self)

    @staticmethod
    def create(army):
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
        result = []
        tokens = getattr(army, cls.__name__.lower())
        for el in tokens:
            for key in el:
                if "add" in key.__name__:
#                    import pdb
#                    pdb.set_trace()
#                    continue 
                    for att in el[key]:
                        key(cls.builder, *att)
                    continue
                key(cls.builder, el[key])
            result.append(cls.builder.build())
            cls.builder.reset_attacks()
        return result

    def __str__(self):
        return "%8s" % (self.name)

class Module(BoardToken):
    pass


class Unit(BoardToken):

    builder = UnitBuilder()

    def __init__(self, name, hp, init, attacks, init_segs = 1):
        self.name = name
        self.hp = hp
        self.initiative = init
        self.attacks = {}
        self.init_segs = init_segs
        for i in attacks:
            print 'sdjfgdjkss', i
            self.attacks.setdefault(i[0], []).append(i[1])

    def attack(self, board, hex_):
        print "Atak", self.attacks
        for i, v in self.attacks.items():
            print "Pierwsza petla"
            lof = list(board.get_line_of_fire(hex_, (i+hex_.content[1]) % 6))
            if not lof:
                continue
            for j in v:
#                import pdb
#                pdb.set_trace()
                print self
                if not j.is_range:
                    print lof[0].content[0].hp
                    lof[0].content[0].hp-=1 
                    print lof[0].content[0].hp
                else:
                    print "NIEEEEE"
class Army(object):

    def __init__(self, name):
        self.name = name


class Moloch(Army):
    exectokens = {Battle: 4, Move: 1, Push: 5, Bomb:1}
    unit = [{UnitBuilder.set_name: "Lowca", UnitBuilder.set_initiative: 3, UnitBuilder.add_attack: [(False, 1, x) for x in (0, 1, 3, 5)], UnitBuilder.set_hp: 1},
            {UnitBuilder.set_name: "Opancerzony_Wartownik", UnitBuilder.set_initiative: 2, UnitBuilder.add_attack: [(True, 1, 1),(True, 1, 5)]},
            {UnitBuilder.set_name: "Klaun", UnitBuilder.add_attack: [(False, 1, 0),(False, 1, 5)], UnitBuilder.set_hp: 2},
            {UnitBuilder.set_name: "Wartownik", UnitBuilder.add_attack: [(True, 1, 0),(True, 1, 5)]},
            {UnitBuilder.set_name: "Dzialko_Gaussa", UnitBuilder.set_initiative: 1, UnitBuilder.add_attack: [(True, 1, 0)]},
            {UnitBuilder.set_name: "Cyborg", UnitBuilder.set_initiative: 3, UnitBuilder.add_attack: [(True, 1, 0)], UnitBuilder.set_hp: 3}]


class Borgo(Army):
    exectokens = {Battle: 6, Move: 4, Granate: 1}
    unit = [{UnitBuilder.set_name: "Mutek", UnitBuilder.set_initiative: 2,
             UnitBuilder.add_attack: [(False, 1, x) for x in (0, 1, 5)]},
            {UnitBuilder.set_name: "Nozownik", UnitBuilder.set_initiative: 3,
             UnitBuilder.add_attack: [(False, 1, 0), (False, 1, 5)]},
            {UnitBuilder.set_name: "Zabojca", UnitBuilder.set_initiative: 3,
             UnitBuilder.add_attack: [(True, 1, 0)]}]


class Posterunek(Army):
    exectokens = {Battle: 6, Move: 7, Sniper: 1}
    unit = [{UnitBuilder.set_name: "Komandos", UnitBuilder.set_initiative: 3, UnitBuilder.add_attack: [(False, 1, 0)]},
            {UnitBuilder.set_name: "CKM", UnitBuilder.set_initiative: 1, UnitBuilder.set_init_segs: 2, UnitBuilder.add_attack: [(False, 1, 0)]},
            ]


class Hegemony(Army):
    exectokens = {Battle: 5, Move: 3, Push: 2, Bomb:1}
    unit = [{UnitBuilder.set_name: "Bydlak", UnitBuilder.set_initiative: 2, UnitBuilder.add_attack: [(False, 2, 0), (False, 1, 1), (False, 1, 5)]},
            {UnitBuilder.set_name: "Uniwersalny Zolnierz", UnitBuilder.set_initiative: 3, UnitBuilder.add_attack: [(True, 1, 0),(False, 1, 0)]},
            {UnitBuilder.set_name: "Straznik", UnitBuilder.set_initiative: 2, UnitBuilder.add_attack: [(False, 1, x) for x in (0, 1, 5)], UnitBuilder.set_hp: 2},
            ]


class Attack(object):

    def __init__(self, is_range, n):
        self.is_range = is_range
        self.n = n









