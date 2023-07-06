from src.token import Token
from src.globals import *
from src.position import Position
from src.errors.illegal_char_error import IllegalCharError

class Lexer(object):
    def __init__(self, filename: str, text: str) -> None:
        self.filename: str = filename
        self.text: str = text
        self.pos: Position = Position(-1, 0, -1, filename, text)
        self.current_char: bool = None
        self.advance()
    
    def advance(self) -> None:
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
    
    def make_tokens(self) -> list:
        tokens: list = []
        TOKEN_TYPES: dict = {
            "+": PLUS,
            "-": MINUS,
            "*": MUL,
            "/": DIV,
            "(": LPAREN,
            ")": RPAREN
        }
        BAD_CHARS: list = ["\t", " "]

        while self.current_char != None:
            if self.current_char not in BAD_CHARS:
                if self.current_char in TOKEN_TYPES.keys():
                    tokens.append(Token(TOKEN_TYPES[self.current_char], pos_start=self.pos))
                
                elif self.current_char in DIGITS:
                    tokens.append(self.make_number())

                # Return error
                else:
                    pos_start: Position = self.pos.copy()
                    return [], IllegalCharError(pos_start, self.pos, f"{self.current_char}")
            
            self.advance()
        
        tokens.append(Token(EOF, pos_start=self.pos))
        return tokens, None
    
    def make_number(self) -> Token:
        num_str: str = ""
        dot_count: int = 0
        pos_start: Position = self.pos.copy()

        while self.current_char != None and self.current_char in f"{DIGITS}.":
            if self.current_char == ".":
                if dot_count == 1:
                    break

                dot_count += 1
                num_str += "."
            
            else:
                num_str += self.current_char
        
            self.advance()
        
        if dot_count == 0:
            return Token(INT, int(num_str), pos_start, self.pos)
        
        else:
            return Token(FLOAT, float(num_str), pos_start, self.pos)