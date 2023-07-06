from src.position import Position

class Token(object):
    def __init__(self, type_, value = None, pos_start: Position = None, pos_end: Position = None) -> None:
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        if pos_end:
            self.pos_end = pos_end
        
    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}:{self.value}"
        
        else:
            return f"{self.type}"
