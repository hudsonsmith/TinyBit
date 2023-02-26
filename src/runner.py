class Runner(object):
    def __init__(self, script: str, filename: str) -> None:
        self.script: str = script
        
        # Line number always starts at zero. (0th indexed arrays)
        self.line_number: int = 0
        self.current_line: str = ""

        self.filename: str = filename

        self.memory: dict = {}
        self.types: dict = {
            "int": int,
            "float": float,
            "str": str
        }

        self.operations: dict = {
            "set": self.set,
            "print": self.print
        }
    
    def run(self) -> None:
        # Parse each line.
        for line in self.script:
            self.current_line = line

            op: str = line.split(" ")[0].lower()
            
            if op in list(self.operations.keys()):
                self.operations[op](line)
            
            else:
                self.error(f"Undefined operation, {op.upper()}")

            self.line_number += 1
    
    def error(self, message: str) -> None:
        print(f"Runtime Error in {self.filename}:{self.line_number}\n\t{self.current_line}")
        print(f"\n{message}")

    
    def set(self, line: str) -> None:
        # Get it into chunks.
        parsed: list = line.split(" ")

        # Clean it.
        for i, val in enumerate(parsed):
            parsed[i] = val.lower().strip()

        var_name: str = parsed[1]
        var_type: str = parsed[2]
        value = parsed[4]

        try:
            self.memory[var_name] = self.types[var_type](value)
        
        except:
            self.error(f"Incompatible types for {var_type} and {value}")
    
    
    def print(self, line: str) -> None:
        parsed: list = line.split(" ", 1)

        content: str = parsed[1]

        # Check if the start and the ending of the content is a string.
        if "\"" == content[0] and "\"" == content[-1] or "\'" == content[0] and "\'" == content[-1]:
            print(content[1:-1])

        
    

