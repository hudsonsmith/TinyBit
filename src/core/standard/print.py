def print(self, line: str) -> None:
    parsed: list = line.split(" ", 1)

    content: str = parsed[1]

    # Check if the start and the ending of the content is a string.
    if "\"" == content[0] and "\"" == content[-1] or "\'" == content[0] and "\'" == content[-1]:
        print(content[1:-1])
    
    else:
        print(self.memory[content])