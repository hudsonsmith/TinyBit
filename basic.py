from src.lexer import Lexer
from src.parser import Parser
from src.nodes.bin_op_node import BinOpNode

def run(filename: str, text: str) -> None:
    lexer: Lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()

    if error:
        return None, error

    # Generate AST
    parser: Parser = Parser(tokens)
    ast: BinOpNode = parser.parse()

    return ast.node, ast.error