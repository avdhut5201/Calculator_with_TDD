def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = set(precedence.keys())
    stack = []  # Stack to hold operators and parentheses
    output = []  # List to build the output postfix expression

    def is_operator(token):
        return token in operators

    def get_precedence(op):
        return precedence.get(op, 0)

    def handle_operator(op):
        while (stack and stack[-1] != '(' and
               get_precedence(stack[-1]) >= get_precedence(op)):
            output.append(stack.pop())
        stack.append(op)

    def handle_delimiter(delim):
        if delim == '(':
            stack.append(delim)
        elif delim == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Remove '(' from stack

    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or '.' in token:  # Operand (number or floating point)
            output.append(token)
        elif is_operator(token):
            handle_operator(token)
        elif token in '()':
            handle_delimiter(token)
        else:
            raise ValueError(f"Invalid token: {token}")

    while stack:
        if stack[-1] in '()':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return ' '.join(output)

if __name__ == "__main__":
    expression= "3 + ( 5 * 2 /  7 ) - 2 "
    print(infix_to_postfix(expression))