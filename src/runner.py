class Runner(object):
    def __init__(self, script: str, filename: str) -> None:
        self.script: str = script
        self.current_line: int = 0
        self.filename: str = filename

        self.memory: dict = {}
        self.types: dict = {
            "int": int,
            "float": float,
            "str": str
        }

        self.operations: dict = {
            "set": self.set
        }
    
    def run(self) -> None:
        # Parse each line.
        for line in self.script:
            op: str = line.split(" ")[0]

            if op in list(self.operations.keys()):
                self.operations[op](line)
                self.current_line += 1

    
    def set(self, line: str) -> None:
        # Get it into chunks.
        parsed: list = line.split(" ")

        # Clean it.
        for i, val in enumerate(parsed):
            line[i] = val.lower().strip()

        var_name: str = parsed[1]
        var_type: str = parsed[2]
        value = parsed[3]

        try:
            self.memory[var_name] = self.types[var_type](value)
        
        except:
            print(f"Runtime Error in {self.filename}:{self.current_line}:\n\t{line}")
            print(f"\nIncompatible types for {var_type} and {value}")
        
    

