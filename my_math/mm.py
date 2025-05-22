# Constant
PI=3.141592653589793

# e constant returns the Eular's number: 2.718281828459045
E = 2.718281828459045

# tau constant returns the value of tau, which is 6.283185307179586 or 2 * PI
TAU = 6.283185307179586

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

def min(*args):
    sum = 0

    for number in args:
        sum += number

    return sum

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
    
def gt(x, y):
    if x > y:
        return True
    else:
        return 
    
def lt(x, y):
    if x < y:
        return True
    else:
        return False
    
def ge(x, y):
    if x >= y:
        return True
    else:
        return False
    
def le(x, y):
    if x <= y:
        return True
    else:
        return False

# Bitwise
def band(x, y):
    result = x & y
    return result

def bor(x, y):
    result = x | y
    return result

def bxor(x, y):
    result = x ^ y
    return result

def bnot(x):
    result = ~x
    return result

def bls(x, y):
    if y < 0:
        return f"ValueError: negative shift count"
    else:
        result = x << y
        return result
    
def brs(x, y):
    if y < 0:
        return f"ValueError: negative shift count"
    else:
        result = x >> y
        return result
