
from stub_isInfiix import is_infix_notation
def test_is_infix_notation():
    # Test with valid infix expressions
    assert is_infix_notation("1 + 2 * 3 - 4") == True
    assert is_infix_notation("12.5 + 3.0 * 4 - 5") == True
    # assert is_infix_notation("a + b * c") == True
    # assert is_infix_notation("( a + b ) * ( c - d )") == True
    assert is_infix_notation("12 + 3") == True
    assert is_infix_notation("(1 + 2) * 3") == True
    assert is_infix_notation("{1 + (2 * 3)} - 4") == True
    assert is_infix_notation("[1 + 2] * (3 - 4)") == True
    
    # Test with invalid infix expressions
    assert is_infix_notation("+ 1 2 3") == False
    assert is_infix_notation("1 2 +") == False
    assert is_infix_notation("* 1 2 + 3") == False
    assert is_infix_notation("1 + 2 *") == False
    assert is_infix_notation("(1 + 2) 2 * 3") == False
    

