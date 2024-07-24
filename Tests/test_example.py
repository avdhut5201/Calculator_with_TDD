from Calculator import (
    summation, 
    subtraction, 
    multiplication, 
    division
)

def test_summation():
    """
    Testing Summation function
    """
    assert summation(2, 10) == 12
    assert summation(3, 5) == 8
    assert summation(4, 6) == 10

def test_subtraction():
    """
    Testing Subtraction function
    """
    assert subtraction(8, 2) == 6
    assert subtraction(7, 5) == 2
    assert subtraction(4, 2) == 2

def test_multiplication():
    """
    Testing Multiplication function
    """
    assert multiplication(2, 0) == 0
    assert multiplication(7, 2) == 14
    assert multiplication(10000, 20) == 200000

def test_Division():
    """
    Testing Division function
    """
    assert division(10, 5) == 2
    assert division(70, 10) == 7
    assert division(16, 5) == 3.2
    

