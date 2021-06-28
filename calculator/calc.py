import numbers

current_value = 0


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
        self.current_value = current_value

    def display_current_value(self, current_value):
        """Prints the current value calculated"""
        self.current_value = current_value
        print("Current value:", current_value)

    def add(self, x):
        """Adds a value x to the current value of the calculator"""
        self.x = x
        self.current_value += x
        return self.current_value

    def subtract(self, x):
        """Subtracts a value x from the current value of the calculator"""
        self.x = x
        self.current_value -= x
        return self.current_value

    def multiply(self, x):
        """Multiplies a value x by the current value of the calculator"""
        self.x = x
        self.current_value *= x
        return self.current_value

    def divide(self, x):
        """Divides a value x by the current value of the calculator"""
        self.x = x
        try:
            self.current_value /= x
            return self.current_value
        except ZeroDivisionError as zd:
            raise CalculatorError("You cannot divide by zero") from zd
            return self.current_value

    def nroot(self, x):
        """Calculates the nroot of a value raised to the power of x"""
        self.x = x
        self.current_value **= x
        return self.current_value

    def main(self, current_value):
        """Controls the program"""
        print("Welcome to the calculator program")
        print("Press Ctrl+C to quit")
        self.display_current_value(current_value)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.main(current_value)
    operations = {
        "1": calculator.add,
        "2": calculator.subtract,
        "3": calculator.multiply,
        "4": calculator.divide,
        "5": calculator.nroot,
    }
    while True:
        print("Select an operation to perform")
        for choice, operation in sorted(operations.items()):
            print(f"{choice}: {operation.__name__}")
        operation = input("What operation? ")
        if operation not in operations:
            print("Sorry, that's not a valid choice.")
            continue
        try:
            x = float(input("Enter next value: "))
        except ValueError:
            raise CalculatorError("Input a number, not a string")

        try:
            current_value = operations[operation](x)
            print("The result is: {}\n".format(current_value))
        except CalculatorError as error:
            print(error)
