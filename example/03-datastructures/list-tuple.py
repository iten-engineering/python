# =============================================================================
# Python examples - list and tuples
# =============================================================================

# -----------------------------------------------------------------------------
# List and Tuples
# -----------------------------------------------------------------------------

# You can hold a sequence of objects with **lists** or **tuples**.
# - Tuples are fixed size in nature whereas lists are dynamic.
# - In other words, a tuple is immutable whereas a list is mutable.

# Mutable List (Set, Dict):
l = [1,2,3]              # List class list() is mutable
l[1] = 22                # works fine

# Immutable Tuple:
t = (1,2,3)              # Tuple class tuple() is immutable
# t[1] = 22                # raises TypeError



# -----------------------------------------------------------------------------
# Basic Operations
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# List Initialisierung
# -----------------------------------------------------------------------------
l1 = []                          # []
l2 = [1,2,3]                     # [1, 2, 3]
l3 = list("abc")                 # ['a', 'b', 'c']
l4 = list(range(4))              # [0,1,2,3]

# -----------------------------------------------------------------------------
# Length, min, max, count, index
# -----------------------------------------------------------------------------
a = [9, 7, 9, 15, 12]
print(len(a))             # 5
print(min(a))             # 7
print(max(a))             # 15

print(a.count(9))         # 2
print(a.index(9))         # 0
print(a.index(12))        # 4 (n-1)


# -----------------------------------------------------------------------------
# in, not in
# -----------------------------------------------------------------------------
numbers = [9, 7, 9, 15, 12]

elem = 7
if elem in numbers:
    print("list contains element:", elem)

elem = 99
if elem not in numbers:
    print("list does not contain element:", elem)

# -----------------------------------------------------------------------------
# Element access
# -----------------------------------------------------------------------------

numbers = (1,2,3,4,5)
n = len(numbers)

print(type(numbers))
print(n)

print( numbers[0] )     # first element
print( numbers[-1] )    # last element
print( numbers[-2] )    # 2nd-last element
print( numbers[-n] )    # first element where n = len(mumbers)


# -----------------------------------------------------------------------------
# Slicing
# -----------------------------------------------------------------------------
# - Slicing : [von:bis:schritt]

numbers = (1,2,3,4,5)

print( numbers[:3] )    # first 3 elements
print( numbers[-2:] )   # last 2 elements

print( numbers[::2] )   # every 2nd element
print( numbers[1:10:2]) # every 2nd from 1 to 10
print( numbers[::] )    # all elements in sequence

first, second = numbers[:2]
print(first, second)


# -----------------------------------------------------------------------------
# Slicing II
# -----------------------------------------------------------------------------
n = 20
r = list(range(n))
print("r         = ", r)
print("r[1:-2:3] = ",r[1:-2:3])

s = r[::3]
print("s         = ", s)
print("s[1:-2]   = ",s[1:-2])

print("r[::3][1:-2]",r[::3][1:-2])


# -----------------------------------------------------------------------------
# Add list items
# -----------------------------------------------------------------------------
# - li.append(el) : fügt ein Element el am Ende der Liste li ein
# - li.insert(pos, el) : fügt ein Element el an der Position pos der Liste li ein
# - li.extend(seq)     : fügt alle Elementen von seq am Ende der Liste li ein.

data = []
data.append("Hello")
data +=  ["word"]
print(data)

data.insert(1, "wonderful")
print(data)

data.extend(["Life", "is", "awesome"])
print(data)

# -----------------------------------------------------------------------------
# Delete list items:
# -----------------------------------------------------------------------------
# - li.pop()    : das letzte Element wird von li herausgenommen und zurückgegeben.
# - li.pop(pos) : das Element an der Position pos wird von li herausgenommen und zurückgegeben.
# - li.remove(el) : das Element el wird von li gelöscht.

items = [1, 2, 3, 4]
e = items.pop()
print(e)                # 4
print(items)            # [1, 2, 3]

e = items.pop(0)
print(e)                # 1
print(items)            # [2, 3]

items = [1, 2, 1, 7]
items.remove(1)
print(items)
print(items)            # [2, 1, 7]

# -----------------------------------------------------------------------------
# Nested lists
# -----------------------------------------------------------------------------
# - Listen können andere Listen enthalten (nested list)
# - Man kann dann mit nested for-loops über die Elemente iterieren

nested = [[1, 2], [10, 20]]
for sublist in nested:
    for elem in sublist:
        print(elem)

# -----------------------------------------------------------------------------
# range, random
# -----------------------------------------------------------------------------
# - range()         : definiert einen iterator über Ganzzahlen
# - range(n)        : von 0 zu n-1
# - range(i,n)      : von i zu n-1
# - range(i,n,step) : von i zu n-1, mit einem Schritt von step

n = 20
range_list = list(range(n))

import random
rand_list = [random.randint(0, 4) for el in range(n)]


# -----------------------------------------------------------------------------
# sort
# -----------------------------------------------------------------------------
# - li.sort() : Die Liste li sortieren (reverse Parameter kontrolliert die Richtung der Sortierung)
# - sorted(li): gibt eine sortierte Liste zurück (reverse Parameter kontrolliert die Richtung der Sortierung)

items = [1, 2, 0, 7]
items.sort()                 # [0, 1, 2, 7]
items.sort(reverse = True)   # [7, 2, 2, 0]
sorted(items)                # [0, 1, 2, 7]
sorted(items,reverse = True) # [7, 2, 2, 0]

# Sort a String-List
words = "cheese, spam, egg, spam, bacon, spam"
sorted_words = sorted(words.split(", "))
sorted_words = ", ".join(sorted_words)
print(sorted_words)


# -----------------------------------------------------------------------------
# map, filter, lambda
# -----------------------------------------------------------------------------

# map(function, iteratable)
# - wendet die Funktion function auf jedes Element von iteratable an.
# - In python3 gibt sie ein generator zurück

gen = map(abs, [-1, 2, -3])
for el in gen:
    print(el)

list( map(abs, [-1, 2, -3]) )           # [1, 2, 3]
list( map(min, [(1,2),(8,5)]) )         # [1, 5]
list( map(sorted, [(1,5,3), (8,5,2)]))  # [[1, 3, 5], [2, 5, 8]]


# filter(function, iteratable)
# - behält alle Elemente el für welche bool(function(el)) == True.
# - In python3 gibt sie ein generator zurück

def isPositiv(x):
    return x > 0;

print(list(filter(isPositiv, [-1,0,1,2])))   # [1, 2]

# Spezieller Anwendungsfall:
print( list(filter(min, [(1,0),(8,-1)])) )  # [(8,-1)]


# lambda arguments : expression
# - Für jedes Filtering eine Funktion definieren macht wenig Sinn
# - Die elegante Lösung ist eine anonyme lambda Funktion
# - Kann direkt in einer map oder filter Anweisung definiert werden
# - Die anonyme lambda wird eigentlich im namespace der Funktion einer Variablen zugewiesen
# - Man kann eine lambda Funktion auch einer Variablen zuweisen
def calc(x,y):
    return x* y

calc2 = lambda x, y: x * y

# Filtern mit lambda:
data = [1, None, 2, 3]
print(data)

print (list(filter(lambda value: value is not None, data)))

notNone = lambda value : value is not None
print (list(filter(notNone, data)))

# -----------------------------------------------------------------------------
# list-comprehension
# -----------------------------------------------------------------------------
# - Eine comprehension ist eine elegante Syntax um Listen, Dictionaries und Sets zu generieren

l1 = [1,2,3]
print(l1)

l2 = []
for e in l1:
    l2.append(e*e)
print(l2)

l3 = [e * e for e in l1]
print(l3)

# Comprehension mit Konditionen

l1 = [1,2,3]
print(l1)                               # [1,2,3]

l2 = []
for e in l1:
    if e != 2:
        l2.append(e*e)
print(l2)                               # [1, 9]

l3 = [e * e for e in l1 if e != 2]
print(l3)                               # [1, 9]

# =============================================================================
# The end.
