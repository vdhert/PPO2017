class Match(object):
    def __init__(self,board):
        self.board = board
        
    def battle(self):
        segments = {}
        for hexxx in self.board.iter_occupied():
            segments.setdefault(hexxx.content[0].initiative, []).append(hexxx)
        print segments
        for segment in sorted(segments, reverse=True):
            for hex_ in segments[segment]:
                hex_.content[0].attack(self.board, hex_)
            
            for hexxx in self.board.iter_occupied():
                if hexxx.content[0].hp <= 0:
                    hexxx.content = None
                    #TODO do dopisania wyrzucanie zetonu do odrzuconych

class TokenContainer(object):
    def __init__(self, listoftokens):
        self.tokens = listoftokens

class Hand(TokenContainer):
    pass

class Graveyard(TokenContainer):
    pass

class Stack(TokenContainer):
    def pop(self):
        firsttoken = self.tokens[0]
        self.Tokens = self.tokens[1:]
        return firsttoken
