# =============================================================================
# Python examples - sets
# =============================================================================

# Set
# - Ein set ist eine ungeordnete Sammlung von eindeutigen Objekten.


# Initialisierung
s = set()            # {}
s = set([1,2,3])     # {1, 2, 3}
s = set([1,2,3,1])   # {1, 2, 3}
s = set("sam")       # {'s','a','m'}

l1 = [1, 2, 3, 2, 6, 2]
s1 = set(l1)         # {1, 2, 3, 6}


# Insert, Update, Delete
s = set([1,2,3])    # {1, 2, 3}
s.add(4)            # {1, 2, 3, 4}
s.add(0)            # {0, 1, 2, 3, 4}
e = s.pop()         # {1, 2, 3, 4}, e=0
s.remove(3)         # {1, 2, 4}


# Union, Intersection, Difference
s1 = set([1,2,3])
s2 = set([1,4])

s = s1.union(s2)           # s = {1, 2, 3, 4}
s = s1.intersection(s2)    # s = {1}
s = s1.difference(s2)      # s = {2, 3}
s = s2.difference(s1)      # s = {4}


# set-comprehension
l = [1, 1, 2, 3, 2]
print(l)

s1 = set()
for e in l:
    s1.add(e)
print(s1)             # {1, 2, 3}

s2 = {e for e in l}
print(s2)             # {1, 2, 3}

# =============================================================================
# The end.
