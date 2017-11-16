class Hex(object):
    def __init__(self, x, y, board):
        self.content=None
        self.x=x
        self.y=y
        self.board=board


class Board(object):

    def __init__(self):
        self.hexes=[Hex(x, y, self) for x in range(5) for y in range(5) if 1 < x + y < 7]
        self.dict_lines = {0 : (True,  self.get_col),
                      1 : (False, self.get_axis),
                      2 : (False, self.get_row),
                      3 : (False, self.get_col),
                      4 : (True, self.get_axis),
                      5 : (True, self.get_row)}

    def add_token(self, hex_, token, token_orient):
        if hex_.board is not self:
            return
        if hex_.content is not None:
            return
        hex_.content=(token, token_orient)

    def __iter__(self):
        return iter(self.hexes)

    def get_row(self,n):
        return [self.hexes[self.hex_n[(x,y)]] for x in range(5) for y in range(5) if 1 < x + y < 7 and x == n]

    def get_col(self,n):
        return [self.hexes[self.hex_n[(x,y)]] for x in range(5) for y in range(5) if 1 < x + y < 7 and y == n]

    def get_axis(self,n):
        return [self.hexes[self.hex_n[(x,y)]] for y in range(5) for x in range(5) if 1 < x + y < 7 and x + y == n + 2]

    def get_line_of_fire(self,hex_,dir_):
        pass
        #~ list_= optional_rev(dict_lines[dir_][0] , dict_lines[dir_][1](dict_lines[dir_][2]))
        #~ h = 0
        #~ while list_[h]!=hex_: h+=1
        #~ return iter(list_[h+1:])

    def iter_occupied(self):
        return OccupiedHexes(self)


class OccupiedHexes(object):
    def __init__(self, board):
        self.board_hexes=board.hexes
        self.index=0
    
    def __iter__(self):
        return self
        
    def next(self):    
        while not self.board_hexes[self.index].content:            
            self.index += 1
            if self.index > len(self.board_hexes) - 1:
                raise StopIteration        
        self.index += 1
        if self.index > len(self.board_hexes) - 1:
            raise StopIteration    
        return self.board_hexes[self.index - 1]
