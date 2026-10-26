
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # Intentional bug: should multiply, not add
    return a + b


def divide(a, b):
    # Intentional bug: zero should be handled explicitly
    return a / b
