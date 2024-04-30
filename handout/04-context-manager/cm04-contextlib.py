# =============================================================================
# Python context managers - timer context manager
# =============================================================================
#
# Python’s generator functions and the contextlib.contextmanager decorator
# provide an alternative and convenient way to implement the context management
# protocol.
#
# If you decorate an appropriately coded generator function with @contextmanager,
# then you get a function-based context manager that automatically provides
# both required methods, .__enter__() and .__exit__().
#
# References:
# - https://docs.python.org/3/library/contextlib.html
# - https://www.blog.pythonlibrary.org/2021/04/07/pythons-with-statement-and-context-managers/
# - https://realpython.com/python-with-statement/#creating-function-based-context-managers
# =============================================================================

from contextlib import contextmanager

@contextmanager
def file_handler(filename, mode):
    print("Create file handler, run enter: Open file", filename)
    file = open(filename, mode=mode)
    try:
        yield file
    except Exception as e:
        print("Exception:", e)
        print("Run exit: Close file", filename)
        if not file.closed:
            file.close()

with file_handler('data.txt', 'r') as f:
    print(int(next(f)))


# =============================================================================
# The end.
