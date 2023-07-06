from src.position import Position
from src.errors.display_problem import display_problem
from src.colors import Colors

class Error(object):
    def __init__(self, pos_start: Position, pos_end: Position, error_name: str, details: str) -> None:
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name: str = error_name
        self.details: str = details
        self.c: Colors = Colors()
    
    def as_string(self) -> str:
        result = f"  {self.c.red}{self.c.underline}{self.c.bold}Error!{self.c.reset}"
        result += f'\n    {self.c.bold}{self.c.italic}{self.c.cyan}File "{self.c.yellow}{self.pos_start.filename}{self.c.cyan}", line {self.pos_start.ln + 1}{self.c.reset}'
        result += display_problem(self.pos_start.func_text, self.pos_start, self.pos_end)

        return result
    
    def __str__(self) -> str:
        return self.as_string()

