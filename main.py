from ast import IfExp
def collect_inputs():
    inputs = ""
    print("Enter values (press ENTER to stop):")
    
    while True:
        user_input = input()
        if user_input == "":
            break
        if inputs:
            inputs += "\n"
        inputs += user_input
        
    return inputs

# expression=collect_inputs()

def is_balanced(equation):
    stack = []
    opening = set("({[")
    closing = set(")}]")
    matching = {")": "(", "}": "{", "]": "["}
    
    for char in equation:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != matching[char]:
                return False
    
    return not stack

def remove_brackets(expression):
    # Define the brackets to remove
    brackets = set("(){}[]")
    
    #  List comprehension to filter out the brackets
    result = ''.join([char for char in expression if char not in brackets])
    
    return result


def is_infix_notation(expression):
    cleaned_expression=remove_brackets(expression)

    operators = set("+-*/")

    tokens = cleaned_expression.split()
    
    
    if not tokens:
        return False

    expect_operand = True
    
    for token in tokens:
        
        if expect_operand:
            try:
                # Check if the token can be converted to a float (handles integers and floating-point numbers)
                if '.' in token:
                    float(token)
                else:
                    int(token)
                   
            except ValueError:
                # If it can't be converted to float, it's invalid
                return False
            expect_operand = False
        else:
            if token not in operators:
                return False
            expect_operand = True
    
    return not expect_operand

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = set(precedence.keys())
    stack = []  # Stack to hold operators and parentheses
    output = []  # For the output postfix expression

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
    expression=collect_inputs()
    print("Expression is : ")
    print(expression)

    balanced_brackets=is_balanced(expression)

    if (balanced_brackets):
        print("Expression is balanced ")
        valid_notation=is_infix_notation(expression)
        if (valid_notation):
         print(f"Is the expression  is infix notation")
         postfix_expression=infix_to_postfix(expression)
         print(f"Postfix Expression: '{postfix_expression}'")
        else:
            print("Invalid Equation ")
    else:
        print(" Invalid Equation ")


    