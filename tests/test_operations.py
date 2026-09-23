import pytest
from typing import Union  #this allows for multiple data types
from app.operations import Operations

number = Union[int, float]

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),            #adding positive integers
    (0, 0, 0),            #adding zeros
    (-10, 5, -5),         #adding negative and positive integers
    (1.5, 2.5, 4.0),      #adding floats
    (-10.5, 7.3, -3.2),   #adding negative and positive floats 
],
    ids = [
    "adding_positive_integers", 
    "adding_zeros", 
    "adding_negative_and_positive_integers",
    "adding_positive_floats",
    "adding_negative_and_positive_floats"
])

def test_addition(a: number, b: number, expected: number) -> None:
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b} to equal {expected}, but got {result}."
    ## assert addition(1,1) == 2

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),            #subtracting positive integers
    (0, 0, 0),            #subtracting zeros
    (-10, 5, -15),        #subtracting negative and positive integers
    (1.5, 2.5, -1.0),     #subtracting floats
    (-10.5, -7.3, -3.2),  #subtracting negative floats
],
    ids = [
    "subtracting_positive_integers", 
    "subtracting_zeros", 
    "subtracting_negative_and_positive_integers",
    "subtracting_positive_floats",
    "subtracting_negative_floats"
])

def test_subtraction(a: number, b: number, expected: number) -> None:
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to equal {expected}, but got {result}."
    ## assert subtraction(1,1) == 0

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),            #multiplying positive integers
    (0, 12, 0),           #multiplying zeros
    (-10, 5, -50),        #multiplying negative and positive integers
    (1.5, 2.5, 3.75),     #multiplying floats
    (-10.5, 7.5, -78.75), #multiplying negative and positive floats 
    (-12, -7, 84)         #multiplying negative integers
],
    ids = [
    "multiplying_positive_integers", 
    "multiplying_zeros", 
    "multiplying_negative_and_positive_integers",
    "multiplying_positive_floats",
    "multiplying_negative_and_positive_floats",
    "multiplying_negative_integers"
])

def test_multiplication(a: number, b: number, expected: number) -> None:
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to equal {expected}, but got {result}."
    ## assert multiplication(1,1) == 1

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),            #dividing positive integers   
    (-12, -4, 3),         #dividing negative integers
    (1.5, 0.5, 3.0),      #dividing floats
    (-10.5, 7.0, -1.5),   #dividing negative and positive floats
    (0, 12,0),            #dividing zero by a positive integer
],
    ids = [
    "dividing_positive_integers",
    "dividing_negative_integers",
    "dividing_floats",
    "dividing_negative_and_positive_floats",
    "dividing_zero_by_positive_integer"
    ])

def test_division_positive(a: number, b: number, expected: number) -> None:
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to equal {expected}, but got {result}."
   ## assert division(1,1) == 1

## def test_division_negative():
   ## with pytest.raises(ZeroDivisionError):
    ## division(1,0)

@pytest.mark.parametrize("a, b", [
    (2, 0),              #dividing by zero
    (-2, 0),             #dividing negative by zero
    (0, 0)               #dividing zero by zero 
],
    ids = [
    "dividing_positive_by_zero",
    "dividing_negative_by_zero",
    "dividing_zero_by_zero"
])

def test_division_by_zero(a: number, b: number) -> None:
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(a, b)
    assert "Division by zero is not allowed." in str(excinfo.value), f"Expected ValueError message 'Division by zero is not allowed.', but got {excinfo.value}."
    ## division(1,0)
