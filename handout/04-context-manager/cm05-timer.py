# =============================================================================
# Python context managers - timer context manager
# =============================================================================
#
# Measure the execution time of the with block.
#
# The __enter__() method may optionally return an object.  If so, Python
# assigns the returned object the ctx.
# - Notice that ctx references the object returned by the __enter__() method.
# - It doesn’t reference the instance of the ContextManager class.
#
# References:
# - https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# - https://www.pythontutorial.net/advanced-python/python-context-managers/
# =============================================================================

from time import perf_counter

class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False

def fibonacci(n):
    f1 = 1
    f2 = 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2
    return f1


with Timer() as t:
    for _ in range(1, 10000):
        fibonacci(1000)

print("Time elapsed:")
print(t.elapsed)

# =============================================================================
# The end.
