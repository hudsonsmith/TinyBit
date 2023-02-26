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

