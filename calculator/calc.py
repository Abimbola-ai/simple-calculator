import numbers


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

    def __init__(self) -> None:
        self._current_value = 0

    @property
    def current_value(self) -> float:
        """A getter function"""
        return self._current_value

    @current_value.setter
    def current_value(self, a: float) -> float:
        """A setter function"""
        try:
            float(a)
            self._current_value = a
        except ValueError:
            raise CalculatorError("Your current value must be numeric")

    def add(self, x: float) -> float:
        """Adds a value x to the current value of the calculator"""
        self.validate(x)
        self._current_value += x
        return self.current_value

    def subtract(self, x: float) -> float:
        """Subtracts a value x from the current value of the calculator"""
        self.validate(x)
        self._current_value -= x
        return self.current_value

    def multiply(self, x: float) -> float:
        """Multiplies a value x by the current value of the calculator"""
        self.validate(x)
        self._current_value *= x
        return self.current_value

    def divide(self, x: float) -> float:
        """Divides a value x by the current value of the calculator"""
        self.validate(x)
        try:
            self._current_value /= x
            return self.current_value
        except ZeroDivisionError as zd:
            raise CalculatorError("You cannot divide by zero") from zd

    def nroot(self, x: float) -> float:
        """Calculates the nroot of a value raised to the power of x"""
        self.validate(x)
        if self.current_value > 0:
            self._current_value **= 1 / x
            return self.current_value
        else:
            raise CalculatorError("Please enter a positive value")

    def validate(self, x: float) -> float:
        try:
            return float(x)
        except:
            raise CalculatorError("Please enter a numeric value")


if __name__ == "__main__":
    c = Calculator()
    c.current_value = 9
    print(c.add(6))
    print(c.subtract(7))
    print(c.multiply(3))
    print(c.divide(2))
    print(c.subtract(50))
    print(c.nroot(-2))
