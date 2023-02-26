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
            "print": self.print,
            "read": self.read
        }
    
    def run(self) -> None:
        # Parse each line.
        for line in self.script:
            self.current_line = line

            if line[0:2] == "//" or line.strip() == "":
                self.line_number += 1
                continue

            op: str = line.split(" ")[0].lower()
            
            if op in list(self.operations.keys()):
                self.operations[op](line)
            
            else:
                self.error(f"Undefined operation, {op.upper()}")
                exit()

            self.line_number += 1
    
    def error(self, message: str) -> None:
        print(f"Runtime Error in {self.filename}:{self.line_number}\n\t{self.current_line}")
        print(f"\n{message}")

    
    def set(self, line: str) -> None:
        # Get it into chunks.
        parsed: list = line.split(" ", 4)

        if len(parsed) > 5:
            self.error("Invalid syntax, to many arguments!")

        # Clean it.
        for i, val in enumerate(parsed[0:-2]):
            parsed[i] = val.lower().strip()

        var_name: str = parsed[2]
        var_type: str = parsed[1]
        value = parsed[4]




        try:
            op: str = value.split(" ")

            # If it's an op
            if op[0].lower() in list(self.operations.keys()):
                args: str = f"{op[0].lower()}"

                for val in op[1:]:
                    args += f" {val}"

                var = self.operations[op[0].lower()](args)


            else:
                var = self.types[var_type](value)
                
                if type(var) == str:
                    var: str = var[1:-1]
            
            self.memory[var_name] = var
            
        
        except:
            self.error(f"Incompatible types for {var_type} and {value}")
    
    
    def print(self, line: str) -> None:
        parsed: list = line.split(" ", 1)

        content: str = parsed[1]

        # Check if the start and the ending of the content is a string.
        if "\"" == content[0] and "\"" == content[-1] or "\'" == content[0] and "\'" == content[-1]:
            print(content[1:-1])
        
        else:
            print(self.memory[content])


    def read(self, line: str) -> str:
        text: str = line.split(" ", 1)[1]

        if "\"" == text[0] and "\"" == text[-1] or "\'" == text[0] and "\'" == text[-1]:
            answer: str = input(f"{text[1:-1]}")
            return answer
        
        else:
            self.error("Only accepts STR inputs")
