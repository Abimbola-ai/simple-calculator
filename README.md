# Simple maths calculator

Simple math calculator for your everyday use.

## Installation

Use a python interface 
and run ```pip install git+https://github.com/Abimbola-ai/simple-calculator.git``` to download all files.

## Usage

### How to create a calculator?

Example code below will create the calculator method for five different operations.

```from calculator import calc
current_value = 0
memory = current_value
current_value_list = [current_value]
calculator = calc.Calculator()
calculator.main(current_value, memory, current_value_list)
   
operations = {
        "1": calculator.add,
        "2": calculator.subtract,
        "3": calculator.multiply,
        "4": calculator.divide,
        "5": calculator.nroot
    }
while True:
  print("Select an operation to perform")
  for choice, operation in sorted(operations.items()):
    print(f"{choice}: {operation.__name__}")
  operation = input("What operation? ")
  if operation not in operations:
    print("Sorry, that's not a valid choice.")
    continue


  x = float(input("Enter next value: "))

  try:
    current_value = operations[operation](x, current_value, current_value_list)
    print("The result is: {}\n".format(current_value))
  except CalculatorError as error:
    print(error)
```

What is what:
- [CalculatorModule](/calculator/calc.py) contains the calculation algorithm;
- [test](/tests/calculator_test.py) contains the `pytest` configuration for the `CalculatorModule`;


### How to calculate?

Select the operation you want to perform, using the instructions that get printed out.
The calculate default value is 0.



### More ideas how to use and extend calculator

- Undo the calculator 3 steps before;
- Reset memory without having to restart the calculator;
- Recall previous memory;
