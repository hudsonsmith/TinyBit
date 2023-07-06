from src.token import Token
from src.nodes.number_node import NumberNode

class BinOpNode(object):
    def __init__(self, left_node: NumberNode, operation_token: Token, right_node: NumberNode) -> None:
        self.left_node = left_node
        self.operation_token: Token = operation_token
        self.right_node = right_node
    
    def __str__(self) -> str:
        return f"({self.left_node}, {self.operation_token}, {self.right_node})"