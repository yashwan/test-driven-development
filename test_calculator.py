import pytest
from calculator import StringCalculator
string_calculator = StringCalculator()
def test_empty_string_returns_zero_in_add():
    assert string_calculator.add("") == 0

def test_single_number_returns_number():
    assert string_calculator.add("1") == 1

def test_two_numbers_returns_sum():
    assert string_calculator.add("1,5") == 6

def test_multiple_numbers_returns_sum():
    assert string_calculator.add("1,2,3,4") == 10

def test_newline_as_delimiter():
    assert string_calculator.add("1\n2,3") == 6

def test_custom_delimiter():
    assert string_calculator.add("//;\n1;2") == 3

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError, match="Negative numbers not allowed: -4"):
        string_calculator.add("1,-4")

def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="Negative numbers not allowed: -2,-5"):
        string_calculator.add("-2,3,-5")

# Substraction
def test_empty_string_returns_zero_in_substract():
    assert string_calculator.substract("") == 0

def test_single_number_returns_number_in_sub():
    assert string_calculator.substract("-1") == -1

def test_two_numbers_returns_sum_in_sub():
    assert string_calculator.substract("-1,-5") == -6

def test_multiple_numbers_returns_sum_in_sub():
    assert string_calculator.substract("-1,-2,-3,-4") == -10

def test_positive_numbers_throw_exception():
    with pytest.raises(ValueError, match="positives numbers not allowed: 1"):
        string_calculator.substract("1,-4")