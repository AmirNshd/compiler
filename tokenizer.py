from errors import InvalidToken
from token_class import Token, tokens, possible_tokens
from token_type import TokenType
import re  # Import regex for complex number/literal matching


def identifier_end(text: str) -> int:
    if not text[0].isalpha() or text[0].upper() != text[0]:
        raise InvalidToken("Variable should start with an uppercase letter")

    text = text[1:]
    for i, char in enumerate(text):
        if char.isalnum():
            continue
        return i + 1
    return len(text) + 1


def number_end(text: str) -> int:
    point = False  # Tracks if a decimal point is present
    exp = False    # Tracks if an exponent (e/E) is present
    digit_after_exp = False  # Tracks if there are digits after the exponent

    for i, char in enumerate(text):
        if char.isnumeric():
            if exp:  # If we're parsing after 'e', validate digit presence
                digit_after_exp = True
            continue
        elif char == '.' and not point and not exp:
            point = True  # Allow a single decimal point
            continue
        elif char in 'eE' and not exp:  # Allow exponent only once
            exp = True
            if i + 1 < len(text) and text[i + 1] in '+-':  # Handle signs after 'e'
                continue
        elif char in '+-' and exp and not digit_after_exp:
            continue  # Allow signs directly after 'e'
        else:
            if exp and not digit_after_exp:
                raise InvalidToken("Exponent must be followed by digits")
            return i

    if exp and not digit_after_exp:
        raise InvalidToken("Exponent must be followed by digits")
    return len(text)


def literal_end(text: str) -> int:
    if not text.startswith('"'):
        raise InvalidToken("Literal must start with a double quote")

    for i in range(1, len(text)):
        if text[i] == '"' and text[i - 1] != '\\':  # End of unescaped quote
            return i + 1
    raise InvalidToken("Unterminated literal")


def tokenize(text: str, line: int = 0, ind: int = 0) -> list[Token]:
    token_list = []  # Accumulated tokens
    while text:
        try:
            token_type = None
            end = None
            end_func = None

            match text[0]:
                case '$':
                    token_type = TokenType.IDENTIFIER
                    end_func = identifier_end
                case char if char.isnumeric():
                    token_type = TokenType.NUMBER
                    end_func = number_end
                case '"':
                    token_type = TokenType.LITERAL
                    end_func = literal_end
                case '+' | '-' | '*' | '/' | '^':
                    token_type = TokenType.OPERATOR
                    end = 1
                case '[' | ']' | '(' | ')' | ';' | '{' | '}':
                    token_type = TokenType.DELIMITER
                    end = 1
                case _:
                    if not possible_tokens.get(text[0]):
                        raise InvalidToken(f"Unknown token at line {line} index {ind}")
                    for token in possible_tokens[text[0]]:
                        if text.startswith(token.value):
                            token_type = token.type
                            end = len(token.value)
                            break
                    if not token_type:
                        raise InvalidToken(f"Unknown token at line {line} index {ind}")

            if not end:
                end = end_func(text[1:]) + 1

            token = Token(token_type, text[:end])
            token.set_indices(ind, ind + end)
            token_list.append(token)
            text = text[end:]
            ind += end

        except InvalidToken as e:
            # Record error and skip the invalid token
            print(f"Error: {e}, skipping token at line {line} index {ind}")
            text = text[1:]  # Skip the problematic character
            ind += 1

    return token_list
