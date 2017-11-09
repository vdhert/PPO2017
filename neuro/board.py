class Hex(object):
    def __init__(self, x, y, board):
        self.content=None
        self.x=x
        self.y=y
        self.board=board
    

class Board(object):
    def __init__(self):
        self.hexes=[Hex(x, y, self) for x in range(5) for y in range(5) if 1 < x + y < 7]

    def add_token(self, hex_, token, token_orient):
        if hex_.board is not self:
            return
        if hex_.content is not None:
            return
        hex_.content=(token, token_orient)

