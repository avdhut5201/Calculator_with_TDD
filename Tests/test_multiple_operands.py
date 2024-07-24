from Calculator_with_args import (summationwithargs,subtractionwithargs,multiplicationargs,divsionwithargs)
import pytest as pt
def test_summation():
    """
      Testing Summation function
    """
    assert summationwithargs(1,2,3)==6

def test_subtraction_multiple_operands():
    """
      Testing Subtraction function with multiple operands
    """
    assert subtractionwithargs(2,1)==1
    assert subtractionwithargs(10,7,3)==0
    assert subtractionwithargs(11,7,5)==-1

def test_multiplication_multiple_operand():
    assert multiplicationargs(10,10,10)==1000
    assert multiplicationargs(10,10,1)==100
    assert multiplicationargs(11,11,0)==0

def test_division_multiple_operand():
   assert divsionwithargs(10,5,2)==1

def test_division_by_zero():
    with pt.raises(ZeroDivisionError):
        divsionwithargs(10,5,0)




