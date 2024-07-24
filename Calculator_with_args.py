def summationwithargs(*num1: int) -> int:
    """
     Calculate the summation of two number
    """
    result=0
    for x in num1:
        result+=x
    return result

def subtractionwithargs(*num1: int) -> int:
    """
    Calculate the subtraction of two numbers
    """
    result = num1[0]
    for x in range(1, len(num1)):
        result -= num1[x]
        print(result)
    return result

def multiplicationargs(*num1):
    """
    Calculate the multiplication of two numbers
    """
    result = 1
    for x in num1:
        result*=x
    return result

def divsionwithargs(*num1) :
    """
    Calculate the subtraction of two numbers
    """
    result = num1[0]
    for x in range(1, len(num1)):
        result /= num1[x]
    return result



    

    