from src.token import Token

class NumberNode(object):
    def __init__(self, token: Token) -> None:
        self.token: Token = token
    
    def __str__(self) -> str:
        return f"{self.token}"