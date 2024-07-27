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

print("Enter the equation")

equation=input()
valid=is_balanced(equation)

if(valid):
    print(f" Equation  is '{equation}' balanced")
else:
    print(f" equation is '{equation}' unbalanced ")
#
