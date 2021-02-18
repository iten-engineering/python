# =============================================================================
# Python examples - constructor
# =============================================================================

# Types of constructors :
# - default constructor
# - parameterized constructor

# Default Constructor
# - The default constructor is simple constructor which doesn’t accept any arguments.
# - It’s definition has only one argument which is a reference to the instance being constructed.

# Parameterized constructor
# - Constructor with parameters is known as parameterized constructor.
# - The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

# -----------------------------------------------------------------------------
# Default consturctor
# -----------------------------------------------------------------------------

class GeekforGeeks:

    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

# -----------------------------------------------------------------------------
# Parameterized constructor
# -----------------------------------------------------------------------------

class Addition:

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
        self.answer = 0

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()

# =============================================================================
# The end.
