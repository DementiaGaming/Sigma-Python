import tokenize
import io
import argparse
import os

# input file handling

def validate_txt_file(file_path):
    if not file_path.endswith('.spy'):
        raise argparse.ArgumentTypeError("Only .spy files are allowed.")
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError("File does not exist.")
    return file_path

parser = argparse.ArgumentParser(description="Only accept a .spy file.")
parser.add_argument('input_file', type=validate_txt_file, help='Path to a .spy file')

args = parser.parse_args()

with open(args.input_file, "r")as file:
    inputCode = file.read()

# rest is converter

keywords = {
    "yap": "print",
    "chatIsThisReal": "if",
    "goon": "while",
    "ahh": "as",
    "cap": False,
    "nocap": True,
    "skibidi": "def",
    "edge": "continue",
    "pullup": "import",
    "sus": "not",
    "aura": "and",
    "clapped": "break",
    "bet": "return",
    "lowkey": "elif",
    "lethimcook": "input",
    "fanumtax": "del",
    "mog": "assert",
    "sigma": "class",
    "cooked": "else",
    "grindset": "for",
    "cringe": "except",
    "based": "finally",
    "crashout": "raise",
    "bruh": "pass",
    "gyatt": "or",
    "deadass": "is",
    "schizo": "nonlocal",
    "lockin": "try",
    "glaze": "global",
    "lit": "in",
    "thicc": "async",
    "rant": "yield",
    "pookie": "with",
    "NPC": None,
    "holup": "await",
    "bop": "lambda",
    "bussin": "from"
}

input_code_io = io.StringIO(inputCode)
modified_tokens = []

for token in tokenize.generate_tokens(input_code_io.readline):
    if token.type == tokenize.NAME and token.string in keywords:
        replacement = str(keywords[token.string])
        token = tokenize.TokenInfo(token.type, replacement, token.start, token.end, token.line)
    modified_tokens.append(token)

# Write the converted Python code
with open("output.py", "w") as out_file:
    out_file.write(tokenize.untokenize(modified_tokens))

# Read and execute the output file
with open("output.py", "r") as file:
    code_in_file = file.read()

exec(compile(code_in_file, '<string>', 'exec'))