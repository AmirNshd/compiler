from tokenizer import tokenize
from errors import InvalidToken

res = ""

with open('text.txt', 'r') as file:

    for i, text in enumerate(file.read().split("\n")):
        text = text.replace(" ", "")
        try:
            tokens = tokenize(text)
        except InvalidToken as e:
            res += f"Invalid Token Error in line {i}: {e}\n"
            tokens = e.partial_tokens  # Collect valid tokens found before the error

        if tokens:
            res += f"line {i} Tokens:\n"
            for token in tokens:
                res += f"\t{token}\n"
        res += '\n'
print(res)