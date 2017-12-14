class Hex(object):
    def __init__(self, x, y, board):
        self.content=None
        self.x=x
        self.y=y
        self.board=board

    def __str__(self):
        if self.content:
            return "[%s|%i]"%(str(self.content[0]),self.content[1])
        return "["+" "*10+"]"

class Board(object):

    lens = [3, 4, 5, 4, 3]

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
    
    def __str__(self):
        result = ""
        y = 0
        for i in self.hexes:
            if y == i.y:
                result += str(i)
            else:
                y = i.y
                result += "\n"+str(i)
        return result

    def __getitem__(self, coords):
        #self.hexes
        pass

    def get_row(self, n):
        return self.hexes[sum(self.lens[:n]): sum(self.lens[:n + 1])]

    def get_col(self, n):
        return []

    def get_axis(self, n):
        return [self.hexes[self.hex_n[(x,y)]] for y in range(5) for x in range(5) if 1 < x + y < 7 and x + y == n + 2]
    
    @staticmethod
    def _opt_rev(rev, lst):
        if rev:
            return list(reversed(lst))
        else:
            return lst

    def get_line_of_fire(self, hex_, dir_):
        dict_args = {0: hex_.y,
                     1: hex_.x + hex_.y - 2,
                     2: hex_.x,
                     3: hex_.y,
                     4: hex_.x + hex_.y - 2,
                     5: hex_.x}
        list_= self._opt_rev(self.dict_lines[dir_][0], self.dict_lines[dir_][1](dict_args[dir_]))
        h = 0
        while list_[h] != hex_: h+=1
        return iter(list_[h+1:])

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
