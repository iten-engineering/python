# =============================================================================
# Python examples - data science library numpy
# =============================================================================

# Die numpy Biblothek stellt die Basisobjekte für technisches Rechnen in python zur Verfügung
# - arrays (ndarray)
# - matrices (matrix)
# Es hat u.a. numpy Funktionen für Mathematik, Statistik und lineare Algebra
# Der Import erfolgt in der Regel mit dem Kürzel np

import numpy as np

b = np.array([6, 7, 8])
print(b)                    # array([6, 7, 8])
print(type(b))              # <class 'numpy.ndarray'>

# -----------------------------------------------------------------------------
# Informationen zum Array
# -----------------------------------------------------------------------------

# ndarray.ndim
# the number of axes (dimensions) of the array.
#
# ndarray.shape
# the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.
#
# ndarray.size
# the total number of elements of the array. This is equal to the product of the elements of shape.
#
# ndarray.dtype
# an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
#
# ndarray.itemsize
# the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
#
# ndarray.data
# the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.
#
# ndarray.reshape
# reshape array elements to the given shape

print("#")
print("# Informationen zum Array")
print("#")

a = np.arange(15).reshape(3, 5)
print(a)                    # [[ 0,  1,  2,  3,  4],           Zweidimensionales Array     ndim = 2
                            #  [ 5,  6,  7,  8,  9],           mit 3 Arrays à 5 Elemente   shape = (3, 5)
                            #  [10, 11, 12, 13, 14]]

print(a.shape)              # (3, 5)
print(a.ndim)               # 2
print(a.dtype.name)         # 'int64'
print(a.itemsize)           # 8
print(a.size)               # 15
print(type(a))              # <class 'numpy.ndarray'>

# -----------------------------------------------------------------------------
# Array creation
# -----------------------------------------------------------------------------

print("#")
print("# Array creation")
print("#")

# a = np.array(1,2,3,4)     # WRONG
                            # Traceback (most recent call last):
                            # TypeError: array() takes from 1 to 2 positional arguments but 4 were given

a = np.array([1,2,3,4])     # RIGHT
print(a)

b = np.array([(1.5,2,3), (4,5,6)])
print(b)                    # [[1.5, 2. , 3. ],
                            #  [4. , 5. , 6. ]]

# The type of the array can also be explicitly specified at creation time:
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)                    # [[1.+0.j, 2.+0.j],
                            #  [3.+0.j, 4.+0.j]]

# Often, the elements of an array are originally unknown, but its size is known.
# Hence, NumPy offers several functions to create arrays with initial placeholder content.
# These minimize the necessity of growing arrays, an expensive operation.
# - zeros  : the function zeros creates an array full of zeros,
# - ones   : the function ones creates an array full of ones,
# - empty  : the function empty creates an array whose initial content is random and depends on the state of the memory.
#            By default, the dtype of the created array is float64.
# - arange : the function arrange creates a range: from, to, step (the to ist exclusive)

x = np.zeros((3, 4))
print(x)

y = np.ones( (3,4), dtype=np.int16 )
print(y)

z = np.empty( (2,3) )
print(z)

a = np.arange(0.0, 1.01, 0.1)      # [0.0 0.1 0.2 ... 0.9 1.0]
print(a)

# -----------------------------------------------------------------------------
# random numbers
# -----------------------------------------------------------------------------

print("#")
print("# Random numbers")
print("#")

# Mit der Random Funktion können Array mit zufälligen Zahlen initalisiert werden

x = np.random.random(3)            # Zahlen zwischen 0..1
print(x)
                                   # Zahlen aus Normalverteilung

y = np.random.normal(loc=0.0, scale=1.0, size=10)
print(y)
                                   # Zahlen aus Auswahl

z = np.random.choice([2,4,6,8], 10)
print(z)

# -----------------------------------------------------------------------------
# Array slicing
# -----------------------------------------------------------------------------

print("#")
print("# Array slicing")
print("#")

# Sample
x = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])

print(x[0, :])              # first line
print(x[:, 0])              # first column
print(x[0, 0])              # first element of first column
print(x[0:2,1])             # first 2 elements of 2nd column

# Onedimensional arrays
a = np.arange(10)**3
print(a)                    # a = [0 1 8 27 64 125 216 343 512 729]
print(a[2])                 # 8
print(a[2:5])               # [8 27 64]

a[0:6:2] = 1000             # from postion 0 to 6 exclusive, set every 2nd element to 1000 (equivalent to: a[:6:2] = 1000)
                            # [1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729]

a[ : :-1]                   # reversed a
                            # [ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000]


# Multidimensional arrays can have one index per axis.
# These indices are given in a tuple separated by commas:
def myfunc(x,y):
    return 10*x + y

b = np.fromfunction(myfunc,(5,4),dtype=int)     # Initialisierung: x = 0...4 mit jeweils y = 0..3
print(a)                                        # [[ 0,  1,  2,  3],
                                                #  [10, 11, 12, 13],
                                                #  [20, 21, 22, 23],
                                                #  [30, 31, 32, 33],
                                                #  [40, 41, 42, 43]]

print(b[2,3])                                   # 23

print(b[0:5, 1])                                # each row in the second column of b (equivalent to: b[ : ,1])
                                                # array([ 1, 11, 21, 31, 41])

print(b[1:3, : ])                               # each column in the second and third row of b
                                                # array([[10, 11, 12, 13],
                                                #        [20, 21, 22, 23]])

# -----------------------------------------------------------------------------
# Operationen per Element (element-wise)
# -----------------------------------------------------------------------------

print("#")
print("# element-wise")
print("#")

# Vergleiche
a = np.array([1,2,3,4,5])
b = a > 3                   # Vergleich "element-wise" erzeugt Array mit boolean
print(b)                    # b = [False False False True True]

c = a[b]                    # Boolean array als Maske
print(c)                    # c = [4 5]

d = a[a <= 3]               # Boolean array als Maske
print(d)                    # d = [1 2 3]


# Operationen wie [+, -, *, /]
a = np.array([20,30,40,50] )

b = a + 5
print(b)

c = a / 5
print(c)

# -----------------------------------------------------------------------------
# Array operations
# -----------------------------------------------------------------------------

print("#")
print("# Array operations")
print("#")

# Arithmetic operators on arrays apply elementwise.
# A new array is created and filled with the result.
a = np.array([20,30,40,50] )
b = np.array([10,15,20,25] )
c = a-b
print(c)   # [10 15 20 25]

# Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays.
# The matrix product can be performed using the @ operator (in python >=3.5) or the dot function
# or method:
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print(A)
print(B)

print(A * B)                       # elementwise product
# array([[2, 0],
#        [0, 4]])
print(A @ B)                       # matrix product
# array([[5, 4],
#        [3, 4]])
print(A.dot(B))                    # another matrix product
# array([[5, 4],
#        [3, 4]])

# -----------------------------------------------------------------------------
# nan (not a number), any and logical functions
# -----------------------------------------------------------------------------

print("#")
print("# nan (not a number), any and logical functions")
print("#")

x  = np.nan                     # undefiniertes Element
y = np.isnan(x)                 # Test für undefiniertes Element
print(y)                        # y = True

a = np.array([1,2,np.nan,4,5])
b= np.isnan(a)                  # Test "element-wise" für undefiniertes Modell
print(b)                        # b = [False False True False False]

c = np.any(b)                   # Prüft ob mindestens ein Eintrag True ist
print(c)                        # c = True

d = np.logical_not(b)           # logical functions (logical_and/not/or/xor)
print(d)                        # d = [True True False True True]


# -----------------------------------------------------------------------------
# Statistics
# -----------------------------------------------------------------------------

print("#")
print("# Statistics")
print("#")

a = np.array([7, 9, 4, 12, 6, 4])

print(np.min(a))
print(np.max(a))
print(np.mean(a))       # Mittelwert
print(np.std(a))        # Standard Abweichung
print(np.sort(a))

# -----------------------------------------------------------------------------
# Further details
# -----------------------------------------------------------------------------

# Links:
# - https://numpy.org/doc/stable/user/quickstart.html

# =============================================================================
# The end.

