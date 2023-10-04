def addition(x = None, y = None):
    return x + y

def subtraction(x = None, y = None):
    return x - y

def multiplication(x = None, y = None):
    return x * y

def division(x = None, y = None):
    if y == 0:
        raise ValueError("Division by zero is not allowed")     # Throw a diff error
    return x / y