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
    "noCap": True,
    "skibidi": "def",
    "edge": "continue",
    "pullUp": "import",
    "sus": "not",
    "aura": "and",
    "clapped": "break",
    "bet": "return",
    "lowkey": "elif",
    "lethimcook": "input",
    "fanumtax": "del",
    "mog": "assert"
}

modifiedCode = []
inputCodeIO = io.StringIO(inputCode)

previousTokenEnd = 0

for token in tokenize.generate_tokens(inputCodeIO.readline):
    currentToken = token.string
    start, end = token.start, token.end

    if start[1] > previousTokenEnd:
        spaces = inputCode[previousTokenEnd:start[0]]
        modifiedCode.append(" ")

    if token.type == tokenize.NAME:
        if currentToken in keywords:
            currentToken = str(keywords[currentToken])
    
    modifiedCode.append(currentToken)

    previousTokenEnd = end[1]

with open("output.py", "w") as file:
    file.write("".join(modifiedCode))

exec(compile("".join(modifiedCode), '<string>', 'exec'))