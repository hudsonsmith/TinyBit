def read(self, line: str) -> str:
    text: str = line.split(" ", 1)[1]

    if "\"" == text[0] and "\"" == text[-1] or "\'" == text[0] and "\'" == text[-1]:
        answer: str = input(f"{text[1:-1]}")
        return answer
    
    else:
        self.error("Only accepts STR inputs")