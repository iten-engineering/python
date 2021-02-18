# Fibonacci numbers module
# Quelle: https://docs.python.org/3/tutorial/modules.html

def print_fib(n):
    """ write Fibonacci series up to n """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib(n):
    """ return Fibonacci series up to n """
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result