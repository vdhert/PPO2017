class Match(object):
    pass

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
