from src.errors.base_error import Error
from src.position import Position

class InvalidSyntaxError(Error):
    def __init__(self, pos_start: Position, pos_end: Position, details="") -> None:
        super().__init__(pos_start, pos_end, "Invalid Syntax", details)