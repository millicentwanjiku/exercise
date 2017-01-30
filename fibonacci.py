"""A program calculates the fibonacci sequence of numbers"""
def fibonacci(number):
    """Afunction that returns the fibonacci value of a number"""
    if type(number) != int:
        return "Only integers are allowed"
    if number < 0:
        return "Only positive numbers are accepted"
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)
