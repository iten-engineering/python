# =============================================================================
# Python examples - classes
# =============================================================================

# Classes and objects
# - everything is an object: "hello".upper()
# - definition via class
# - every class method needs the instance reference `self` as first argument
#   (the name can be anything, but self is used per convention)
# - class attributes are defined implicitly (as with all types)
# - all constructors have the name __init__

class myClass:
    def __init__(self, arg1, arg2):
        self.var1 = arg1
        self.var2 = arg2

    def getVar1(self):
        return self.var1


# create instances
myInstance = myClass("p1", "p2")

# calling a method:
# - note that self is passed implicitly
# - there is no destructor but an automatic garbage collection
result = myInstance.getVar1()

# -----------------------------------------------------------------------------
# Sample
# -----------------------------------------------------------------------------

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# call a object function
myobjectx.function()

# =============================================================================
# The end.
