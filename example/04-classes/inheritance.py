# =============================================================================
# Python examples - inheritance
# =============================================================================

# -----------------------------------------------------------------------------
# Person
# -----------------------------------------------------------------------------

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


# -----------------------------------------------------------------------------
# Teacher
# -----------------------------------------------------------------------------

class Teacher(Person):
    pass            # Use the pass keyword when you do not want to add
                    # any other properties or methods to the class.

# Use the Student class
x = Teacher("Mike", "Olsen")
x.printname()

# -----------------------------------------------------------------------------
# Student with constructor and method:
# -----------------------------------------------------------------------------

class Student(Person):
    def __init__(self, fname, lname, studentId):
        super().__init__(fname, lname)
        self.studentId = studentId

    def printname(self):
        print(self.firstname, self.lastname, self.studentId)

# Use the Student2 class
x = Student("James", "Bond", "007")
x.printname()

# =============================================================================
# The end.
