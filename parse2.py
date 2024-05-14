import re

# Define token patterns
token_patterns = {
    'STRING': r'\".*?\"',  # Matches a string enclosed in double quotes
    'LABEL': r'\.[a-zA-Z_][a-zA-Z0-9_]*',  # Matches a label starting with a dot
    'INSTRUCTION': r'\b[a-zA-Z]+q\b',  # Matches an instruction ending with 'q'
    'REGISTER': r'\%\w+',  # Matches a register starting with '%'
    'DIRECTIVE': r'\.[a-zA-Z_]+',  # Matches a directive starting with a dot
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',  # Matches an identifier
    'NUMBER': r'\$\d+',  # Matches a number starting with '$'
    'COMMENT': r'\;.*',  # Matches a comment starting with ';'
    'NEWLINE': r'\n',  # Matches a newline character
    'WHITESPACE': r'[ \t]+',  # Matches whitespace (spaces and tabs)
    'COMMA': r',',  # Matches a comma
    'SEMICOLON': r';',  # Matches a semicolon
    'COLON': r':',  # Matches a colon
    'OPEN_PAREN': r'\(',  # Matches an open parenthesis
    'CLOSE_PAREN': r'\)',  # Matches a close parenthesis
    'OPEN_BRACKET': r'\[',  # Matches an open bracket
    'CLOSE_BRACKET': r'\]',  # Matches a close bracket
    'PLUS': r'\+',  # Matches a plus sign
    'MINUS': r'-',  # Matches a minus sign
    'MULTIPLY': r'\*',  # Matches a multiply sign
    'DIVIDE': r'/',  # Matches a divide sign
    'EQUAL': r'=',  # Matches an equal sign
    'LESS_THAN': r'<',  # Matches a less than sign
    'GREATER_THAN': r'>',  # Matches a greater than sign
    'UNDERSCORE': r'_',  # Matches an underscore
    'PERCENT': r'%',  # Matches a percent sign
    'AMPERSAND': r'&',  # Matches an ampersand
    'PIPE': r'\|',  # Matches a pipe
    'CARET': r'\^',  # Matches a caret
    'DOLLAR': r'\$',  # Matches a dollar sign
    'AT': r'@',  # Matches an at sign
    'EXCLAMATION': r'!',  # Matches an exclamation mark
    'QUESTION': r'\?',  # Matches a question mark
    'BACKSLASH': r'\\',  # Matches a backslash
    'FORWARD_SLASH': r'/',  # Matches a forward slash
    'QUOTE': r'\'',  # Matches a single quote
    'BACKTICK': r'`',  # Matches a backtick
    'NUMBER': r'\b\d+\b|\$\d+',
    # Add more patterns as needed
}

# Token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Lexer function
# Lexer function
def lexer(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in token_patterns.items():
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'COMMENT':
                    tokens.append(Token(token_type, value))
                code = code[match.end():]
                break
        if not match:
            raise SyntaxError('Illegal character: {}'.format(code[0]))
    return tokens


# Parser function
def parser(tokens):
    parse_tree = []
    while tokens:
        token = tokens.pop(0)
        if token.type == 'LABEL':
            parse_tree.append((token.value, []))
        elif token.type in ['INSTRUCTION', 'DIRECTIVE', 'IDENTIFIER']:
            parse_tree[-1][1].append(token.value)
        elif token.type == 'STRING':
            parse_tree[-1][1].append(token.value)
    return parse_tree

# Function to output the parse tree to a text file
def output_parse_tree(parse_tree, filename):
    with open(filename, 'w') as file:
        for label, contents in parse_tree:
            file.write(label + '\n')
            for content in contents:
                file.write('  ' + content + '\n')

# Main function to read assembly code from a file and create a parse tree
def main(assembly_file_path, output_file_path):
    # Read the assembly code from a file
    with open(assembly_file_path, 'r') as file:
        assembly_code = file.read()

    # Tokenize the assembly code
    tokens = lexer(assembly_code)

    # Parse the tokens into a parse tree
    parse_tree = parser(tokens)

    # Output the parse tree to a text file
    output_parse_tree(parse_tree, output_file_path)

# Specify the path to your assembly code file and the output file
assembly_file_path = 'output.txt'
output_file_path = 'parse_tree.txt'

# Run the main function
if __name__ == '__main__':
    main(assembly_file_path, output_file_path)
