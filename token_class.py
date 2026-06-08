from token_type import TokenType


class Token:
    
    def __init__(
        self,
        type: TokenType,
        value: str,
        start_ind: int,
        end_ind: int) -> None:
        
        self.type = type
        self.start_ind = start_ind
        self.end_ind = end_ind
        self.value = value
        
    def __init__(self, type: TokenType, value: str) -> None:
        self.type = type
        self.value = value
        
    def set_indices(self, start, end):
        self.start_ind, self.end_ind = start, end
        
    def __str__(self):
        return f"[{str(self.type.name)}: {self.value}, ({self.start_ind}, {self.end_ind})]"
    
    
tokens = {
    "if": Token(TokenType.KEYWORD, "if"),
    "while": Token(TokenType.KEYWORD, "while"),
    "until": Token(TokenType.KEYWORD, "until"),
    "repeat": Token(TokenType.KEYWORD, "repeat"),
    "for": Token(TokenType.KEYWORD, "for"),
    "Div": Token(TokenType.OPERATOR, "Div"),
    "dec": Token(TokenType.OPERATOR, "dec"),
    "inc": Token(TokenType.OPERATOR, "inc"),
    '<': Token(TokenType.OPERATOR, '<'),
    "<=": Token(TokenType.OPERATOR, "<="),
    "<>": Token(TokenType.OPERATOR, "<>"),
    '>': Token(TokenType.OPERATOR, '>'),
    ">=": Token(TokenType.OPERATOR, ">="),
    '=': Token(TokenType.OPERATOR, '='),
    "==": Token(TokenType.OPERATOR, "=="),
}

possible_tokens = {} 

for name, token in tokens.items():
    if not possible_tokens.get(name[0]):
        possible_tokens[name[0]] = []
    possible_tokens[name[0]].append(token)
