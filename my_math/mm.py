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

def flr_div(dividend, divisor):
    if divisor == 0:
        return f"ZeroDivisionError: integer division or modulo by zero"
    else:
        floor_quotient = dividend // divisor
        return floor_quotient
    
def exp(base, power):
    if base == 0 and power < 0:
        return f"ZeroDivisionError: 0.0 cannot be raised to a negative power"
    else:
        result = base ** power
        return result

# Comparison
def eq(x, y):
    if x == y:
        return True
    else:
        return False
    
def ne(x, y):
    if x != y:
        return True
    else:
        return False
    