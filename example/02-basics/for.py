# =============================================================================
# Python examples - for loop
# =============================================================================

# break and continue
# - break : loop execution
# - jump  : to next loop iteration

# For loop
for i in range(10):      # i = 0..9
    print(i)

# For loop with range
for i in range(5,10):    # i = 5..9
    print(i)

# For loop with range
for i in range(0,100,10):    # i = 0, 10, 20, ... 80, 90
    print(i)

# For loop with index and element (enumerate)
list = ["first", "second"]
for pair in enumerate(list):
    print(type(pair), pair)     # <class 'tuble'> (0, 'first')
                                # <class 'tuble'> (1, 'second')

# -----------------------------------------------------------------------------
# For loop in reverse order
# -----------------------------------------------------------------------------

words = ["coming","is","winter"]
for word in reversed(words):
    print(word)

# -----------------------------------------------------------------------------
# For loop over mutliple arrays (zip)
# -----------------------------------------------------------------------------

names = ["Peter", "Jane", "Fred"]
ages = [31, 35, 4]

for t in zip(names, ages):              # use a tuple
    print(t)

for name, age in zip(names, ages):      # use multiple loop-variables
    print(name, "is", age)

for i,name in enumerate(names):         # use enumerate and index
    print(name, "is", ages[i])

for i in range(len(names)):             # use range and index
    print(names[i], "is", ages[i])

# =============================================================================
# The end.
