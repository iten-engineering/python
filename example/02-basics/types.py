# =============================================================================
# Python examples - types
# =============================================================================

i = 42
print(type(i))

i = "Hallo"
print(type(i))

i = [3,9,17]
print(type(i))


solution = 42
print(type(solution))
print(isinstance(solution, int))

# -----------------------------------------------------------------------------
# information and help
# -----------------------------------------------------------------------------

obj = str

help(obj)     # show help of this object / function
print(obj)    # print object to default output
type(obj)     # show type of object

dir()         # List all variables of the namespace
dir(obj)      # List all attributes of object instance

c = complex   # class
c.__dict__    # show attributes of class
vars(c)       # show attributes of class

# -----------------------------------------------------------------------------
# show instance attributes
# -----------------------------------------------------------------------------

class Foo(object):
    def __init__(self):
        self.a = 1
        self.b = 2

vars(Foo()) #==> {'a': 1, 'b': 2}
vars(Foo()).keys() #==> ['a', 'b']

# =============================================================================
# The end.