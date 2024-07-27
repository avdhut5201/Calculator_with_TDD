import pytest
from stub_balnced_brackets import is_balanced

def test_is_balanced():
    # Test with balanced brackets
    assert is_balanced("()") == True
    assert is_balanced("()[]{}") == True
    assert is_balanced("{[()]}") == True
    assert is_balanced("a*(b+c)-{d/e}") == True
    
    # Test with unbalanced brackets
    assert is_balanced("(") == False
    assert is_balanced("({[") == False
    assert is_balanced("{[)]}") == False
    assert is_balanced("a*(b+c)-{d/e") == False
    
    # Test with no brackets
    assert is_balanced("abc") == True
    assert is_balanced("123") == True
    assert is_balanced("1+2*3-4") == True
    assert is_balanced("a*(b+c)-{d/e}")==True

    

