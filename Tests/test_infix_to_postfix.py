import pytest
from stub_infix_to_postfix import infix_to_postfix  # Import the function to be tested

def test_basic_operations():
    assert infix_to_postfix("3 + 5") == "3 5 +"
    assert infix_to_postfix("10 + 2 * 6") == "10 2 6 * +"
    assert infix_to_postfix("100 * 2 + 12") == "100 2 * 12 +"
    assert infix_to_postfix("100 * ( 2 + 12 )") == "100 2 12 + *"

def test_complex_operations():
    assert infix_to_postfix("3 + 5 * ( 2 - 8 )") == "3 5 2 8 - * +"
    assert infix_to_postfix("( 1 + 2 ) * ( 3 + 4 )") == "1 2 + 3 4 + *"
    assert infix_to_postfix("( 1 + ( 2 * 4 ) )") == "1 2 4 * +"
    assert infix_to_postfix("(({[12.5 * 2] + 40} / 25.00) * 1)") == '12.5 2 40 25.00 / + * 1 *'

def test_edge_cases():
    assert infix_to_postfix("5") == "5"
    assert infix_to_postfix("2 + 2") == "2 2 +"
    assert infix_to_postfix("2 - 1") == "2 1 -"
    assert infix_to_postfix("3 + 5 * 2 / ( 7 - 2 )") == "3 5 2 * 7 2 - / +"
    assert infix_to_postfix("12.5") == "12.5"


# def test_invalid_expression():
#     with pytest.raises(ValueError):
#         infix_to_postfix("3 + * 2")
#     with pytest.raises(ValueError):
#         infix_to_postfix("3 + ( 2 * 4")
#     with pytest.raises(ValueError):
#         infix_to_postfix(") 1 + 2 (")

