from src.position import Position
from src.colors import Colors

def display_problem(text: str, position_start: Position, position_end: Position) -> str:
    result: str = "    \n"
    lines: list = text.split("\n")
    c: Colors = Colors()

    for i in range(position_start.ln + 1):
        result += f"    {lines[i]}\n"
    
    result += f"    {position_start.col * ' '}{c.purple}{c.bold}^{c.reset}\n"

    return result


        

