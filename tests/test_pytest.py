import pytest

from calculator.calc import CalculatorError, Calculator

# current_value = 0


def test_add():
    """Tests the add function in calculator program"""
    calculator = Calculator()
    current_value = calculator.add(3)
    assert current_value == 3


def test_subtract():
    """Tests the subtract function in calculator program"""
    calculator = Calculator()
    calculator.current_value = 4
    current_value = calculator.subtract(1)
    assert current_value == 3


def test_multiply():
    """Tests the multiply function in calculator program"""
    calculator = Calculator()
    calculator.current_value = 4
    current_value = calculator.multiply(3)
    assert current_value == 12


def test_divide():
    """Tests the divide function in calculator program"""
    calculator = Calculator()
    calculator.current_value = 9
    current_value = calculator.divide(3)
    assert current_value == 3


def test_nroot():
    """Tests the nth root function in calculator program"""
    calculator = Calculator()
    calculator.current_value = 4
    current_value = calculator.nroot(2)
    assert current_value == 2


def test_divide_by_zero():
    """Tests the divide by zero function in calculator program"""
    calculator = Calculator()
    calculator.current_value = 4
    with pytest.raises(CalculatorError):
        result = calculator.divide(0)
