def remove_brackets(expression):
    # Define the brackets to remove
    brackets = set("(){}[]")
    
    # Use a list comprehension to filter out the brackets
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

   
if __name__ == "__main__":
#  expression = "(1 + 2) * {3 + [4 - (5 * 6)]}"
#  cleaned_expression = remove_brackets(expression)
#  print(cleaned_expression)

   expression = "(1 + 2) * 3"
   valid_expression=is_infix_notation(expression)
   if (valid_expression):
        print(f"Is the expression '{expression}' is infix notation")
   else:
          print(f"Is the expression '{expression}' is not a infix notation")

    #print(f"Is the expression '{expression}' in infix notation? {is_infix_notation(expression)}")
