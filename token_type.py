from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    DELIMITER = auto()
    NUMBER = auto()
    LITERAL = auto()
