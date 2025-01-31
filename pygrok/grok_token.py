from enum import Enum 
from typing import Any

class TokenType(Enum):
    #Special 
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    #Data Types 
    IDENT = "IDENT"
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"

    # Arithematic Symbols 
    PLUS = "PLUS"
    MINUS = "MINUS"
    ASTERISK = "ASTRISK"
    SLASH = "SLASH"
    POW = "POW"
    MODULUS = "MODULUS"

    #Assignment Symbols 
    EQ = "EQ"

    # Comparison Symbols 
    LT = '<'
    GT = '>'
    EQ_EQ = '=='
    NOT = '!'
    NOT_EQ = '!='
    LT_EQ = '<='
    GT_EQ = '>='

    #Symbols 
    COLON = "COLON"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    ARROW = "ARROW"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    QUOTE = "QUOTE"

    # Keywords
    LET = "LET"
    FN = "FN"
    RETURN = "RETURN"
    IF = "IF"
    ELSE = "ELSE"
    ELIF = "ELIF"
    TRUE = "TRUE"
    FALSE = "FALSE"

    # Typing
    TYPE = "TYPE"

class Token: 
    def __init__(self, type: TokenType | None = None, literal: Any = None, line_no: int | None = None, position: int |None = None )-> None:
        self.type = type
        self.literal = literal 
        self.line_no = line_no
        self.position = position
    def __str__(self) -> str:
        return f"Token[{self.type} : {self.literal} : Line {self.line_no} : Position {self.position}]"
    def __repr__(self) -> str: 
        return str(self)


KEYWORDS: dict[str, TokenType] = {
    "let": TokenType.LET, 
    "fn": TokenType.FN,
    "return": TokenType.RETURN, 
    "if": TokenType.IF, 
    "else": TokenType.ELSE, 
    "elif": TokenType.ELIF,  
    "true": TokenType.TRUE, 
    "false": TokenType.FALSE
}

ALT_KEYWORDS: dict[str, TokenType] = {
    "pls": TokenType.LET,
    "be": TokenType.EQ,
    "thx": TokenType.SEMICOLON,
    "fn": TokenType.FN,
    "return": TokenType.RETURN,
    "arrow": TokenType.ARROW, 
    "would": TokenType.IF, 
    "otherwise": TokenType.ELSE, 
    "appreciate": TokenType.ELIF,
    "reasonable": TokenType.TRUE, 
    "absurd": TokenType.FALSE
}

TYPE_KEYWORDS: list[str] = ["int", "float", "string"]

def lookup_ident(ident: str) -> TokenType:
    tt: TokenType | None = KEYWORDS.get(ident)
    if tt is not None: 
        return tt

    tt: TokenType| None = ALT_KEYWORDS.get(ident)
    if tt is not None: 
        return tt

    if ident in TYPE_KEYWORDS:
        return TokenType.TYPE

    return TokenType.IDENT
