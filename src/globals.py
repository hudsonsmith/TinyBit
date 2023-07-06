########################################
# TOKENS                               #
########################################

DIGITS: str = "0123456789"

# The "FUN" version below... (Worse runtime) 
# DIGITS: list = [
#     str(i) for i in range(10)
# ]

INT: str = "INT"
FLOAT: str = "FLOAT"
PLUS: str = "PLUS"
MINUS: str = "MINUS"
MUL: str = "MUL"
DIV: str = "DIV"
LPAREN: str = "LPAREN"
RPAREN: str = "RPAREN"
EOF: str = "EOF"