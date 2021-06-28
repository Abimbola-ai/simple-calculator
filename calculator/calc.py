import numbers

# current_value = 0


class CalculatorError(Exception):
    """For calculator errors"""

    pass


class Calculator:
    """
    A class for simple math calculations.
    ...
    Attributes
    ----------
    x: int
        a number used to perform calculations
    current_value: float
        a current value initially set to 0
    """

    def __init__(self):
        self.x = 0
        self.current_value = 0

    def display_current_value(self, current_value):
        """Prints the current value calculated"""
        self.current_value = current_value
        print("Current value:", current_value)

    def add(self, x):
        """Adds a value x to the current value of the calculator"""
        try:
            self.current_value += x
            return self.current_value
        except TypeError:
            raise CalculatorError("Please enter a numeric value")
            return self.current_value

    def subtract(self, x):
        """Subtracts a value x from the current value of the calculator"""
        try:
            self.current_value -= x
            return self.current_value
        except TypeError:
            raise CalculatorError("Please enter a numeric value")
            return self.current_value

    def multiply(self, x):
        """Multiplies a value x by the current value of the calculator"""
        try:
            self.current_value *= x
            return self.current_value
        except TypeError:
            raise CalculatorError("Please enter a numeric value")
            return self.current_value

    def divide(self, x):
        """Divides a value x by the current value of the calculator"""
        try:
            self.current_value /= x
            return self.current_value
        except ZeroDivisionError as zd:
            raise CalculatorError("You cannot divide by zero") from zd
            return self.current_value

    def nroot(self, x):
        """Calculates the nroot of a value raised to the power of x"""
        try:
            self.current_value **= 1 / x
            return self.current_value
        except TypeError:
            raise CalculatorError("Please enter a numeric value")
            return self.current_value
