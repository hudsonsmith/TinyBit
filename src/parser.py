from src.token import Token
from typing import List, Union, Optional
from src.globals import *
from src.nodes.number_node import NumberNode
from src.nodes.bin_op_node import BinOpNode
from src.errors.base_error import Error
from src.errors.invalid_syntax_error import InvalidSyntaxError


class ParseResult(object):
    def __init__(self) -> None:
        self.error: Optional[Error] = None
        self.node: Optional[BinOpNode] = None
    
    def register(self, result) -> None:
        if isinstance(result, ParseResult):
            if result.error:
                self.error = result.error

            return result.node
        
        return result

    def success(self, node: Union[BinOpNode, NumberNode]) -> None:
        self.node = node
        return self
    
    def failure(self, error: Error) -> None:
        self.error = error


class Parser(object):
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens: list = tokens
        self.token_index: int = -1
        self.advance()
    
    def advance(self) -> Token:
        """
        A function used to advance one in the index of tokens.
        """
        self.token_index += 1

        if self.token_index < len(self.tokens):
            self.current_token: Token = self.tokens[self.token_index]
        
        return self.current_token
    
    def parse(self) -> BinOpNode:
        result: BinOpNode = self.expr()
        
        if not result.error and self.current_token.type != EOF:
            return result.failure(
                InvalidSyntaxError(
                    self.current_token.pos_start, self.current_token.pos_end,
                    "Expected '+', '-', '*', or '/'"
                )
            )
        return result
    
    def factor(self) -> NumberNode:
        result: ParseResult = ParseResult()
        token: Token = self.current_token

        # If an integer or a float is found
        # return a number node.
        if token.type in (INT, FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(token))
        
        return result.failure(
            InvalidSyntaxError(
                token.pos_start, token.pos_end,
                "Expected int or float"
            )
        )
    
    def term(self) -> BinOpNode:
        return self.binary_operation(self.factor, (MUL, DIV))
    
    def expr(self) -> BinOpNode:
        return self.binary_operation(self.term, (PLUS, MINUS))
    
    def binary_operation(self, function, operations: tuple) -> BinOpNode:
        """
        A function to get a full binary operation.
        This returns a BinOpNode object

        A term is simply two factors (numbers) joined by one expression.
        """

        result: ParseResult = ParseResult()

        # A factor is just an Integer or a Float
        left_factor: NumberNode = result.register(function())

        if result.error:
            return result

        while self.current_token.type in operations:
            operation_token: Token = self.current_token
            result.register(self.advance())

            right_factor: NumberNode = result.register(function())

            if result.error:
                return result

            left_factor: BinOpNode = BinOpNode(left_factor, operation_token, right_factor)
        
        return result.success(left_factor)