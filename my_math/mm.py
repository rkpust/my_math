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
