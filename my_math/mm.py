# Constant
PI=3.141592653589793

# Arithmetic
def add(*args):
    sum = 0

    for number in args:
        sum += number

    return sum

def sub(x, y):
    result = 0
    result = x - y

    return result

def mul(*args):
    product = 1

    for number in args:
        product *= number

    return product

def div(dividend, divisor):
    if divisor == 0:
        return f"ZeroDivisionError: division by zero"
    else:
        quotient = dividend / divisor
        return quotient
    
def mod(dividend, divisor):
    if divisor == 0:
        return f"ZeroDivisionError: integer division or modulo by zero"
    else:
        remainder = dividend % divisor
        return remainder
    