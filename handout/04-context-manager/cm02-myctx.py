# =============================================================================
# Python context managers - my context manager
# =============================================================================
#
# When you use ContextManager class with the with statement, Python
# implicitly creates an instance of the ContextManager class (instance)
# and automatically call __enter__() method on that instance.
#
# The __enter__() method may optionally return an object.  If so, Python
# assigns the returned object the ctx.
# - Notice that ctx references the object returned by the __enter__() method.
# - It doesn’t reference the instance of the ContextManager class.
#
# If an exception occurs inside the with block or after the with block,
# Python calls the __exit__() method on the instance object.
#
# References:
# - https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# - https://www.pythontutorial.net/advanced-python/python-context-managers/
# =============================================================================


class MyContext:
    def __init__(self):
        print("Create MyContext")

    def __enter__(self):
        print("Run __enter__")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Run __exit__")

        ## Returning a true value from this method will cause the with
        # statement to suppress the exception and continue execution
        # with the statement immediately following the with statement.
        #
        # Otherwise the exception continues propagating after this method
        # has finished executing. The exception passed in should never be
        # reraised explicitly - instead, this method should return a false
        # value to indicate that the method completed successfully and does
        # not want to suppress the raised exception.
        #
        # This allows context management code to easily detect whether or
        # not an __exit__() method has actually failed.
        return False

print("#")
print("# Run business code")
print("#")
with MyContext() as ctx:
    print("execute buisness code 1")
    print("execute buisness code 2")
    print("execute buisness code 3")


print("#")
print("# Run business code with exception")
print("#")
try:
    with MyContext() as ctx:
        print("raise exception")
        x = int("hello")
except ValueError as e:
    print(e)

# =============================================================================
# The end.
