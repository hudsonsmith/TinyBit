
class Position(object):
    def __init__(self, idx: int, ln: int, col: int, filename: str, func_text: str) -> None:
        self.idx: int = idx
        self.ln: int = ln
        self.col: int = col
        self.filename: str = filename
        self.func_text: str = func_text
    
    def advance(self, current_char: str = None) -> None:
        self.idx += 1
        self.col += 1
    
        if current_char == "\n":
            self.ln += 1
            self.col = 0
        
        return self
    
    def copy(self) -> object:
        return Position(self.idx, self.ln, self.col, self.filename, self.func_text)