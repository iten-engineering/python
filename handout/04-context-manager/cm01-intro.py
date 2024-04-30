# =============================================================================
# Python context managers - intro
# =============================================================================
#
# Python’s with statement supports the concept of a runtime context defined
# by a context manager.
#
# This is implemented using a pair of methods that allow user-defined classes
# to define a runtime context that is entered before the statement body is
# executed and exited when the statement ends.
#
# References:
# - https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# - https://www.pythontutorial.net/advanced-python/python-context-managers/
# =============================================================================

def demo1():
    print ("#")
    print ("# Demo 1: Resource leak")
    print ("#")

    print("1. Open file and read data")
    f = open('data.txt')

    print("2. Process data with Exception (string and not a number")
    data = f.readlines()
    print(int(data[0]))

    print ("3. Close file (WILL NOT BE REACHED")
    f.close()

try:
    demo1()
except:
    pass


def demo2():
    print ("#")
    print ("# Demo 2: Resource leak fixed with try finally")
    print ("#")

    try:
        print("1. Open file and read data")
        f = open('data.txt')

        print("2. Process data with Exception (string and not a number")
        data = f.readlines()
        print(int(data[0]))

    finally:
        print ("3. Close file (WILL BE EXECUTED)")
        f.close()

try:
    demo2()
except:
    pass


def demo3():
    print ("#")
    print ("# Demo 3: Resource leak fixed with 'with' statement")
    print ("#")

    print("1. Open file, process data and close file")
    with open('data.txt') as f:
        data = f.readlines()
        print(int(data[0]))


try:
    demo3()
except:
    pass

# =============================================================================
# The end.
