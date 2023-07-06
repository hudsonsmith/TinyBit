from src.position import Position
from src.errors.base_error import Error 

class IllegalCharError(Error):
    def __init__(self, pos_start: Position, pos_end: Position, details: str) -> None:
        super().__init__(pos_start, pos_end, "Illegal Character", details)