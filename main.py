import basic
from src.colors import Colors

c: Colors = Colors()

while True:
    text: str = input(f"{c.red}~{c.yellow}~{c.green}>{c.reset} ")
    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    
    else:
        print(result)
        # print(result.left_node)