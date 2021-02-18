# =============================================================================
# Python examples - dictionaries
# =============================================================================

# Dictionaries
# - Ein dict enthält key:value Paare und ist nicht sortiert.
# - Der Zugriff erfolgt via `key` (Schlüssel).
# - Schlüssel können von verschiedenen Typen sein (ausser list und dict, da veränderlich):
#   - int, float, complex, bool
#   - str, tuple, function

# -----------------------------------------------------------------------------
# Initialisierung
# -----------------------------------------------------------------------------

# Initialisierung mit Literal:
d1 = {}
d2 = {"key":"value", 1:"value 1", 2:"value 2"}

# Initialisierung mit Klasse
d1 = dict()
d2 = dict([ ("key","value of k"), (1, "value of 1"), (2, 4711) ])
d3 = dict([ ["key","value of k"], [1, "value of 1"], [2, 4711] ])

# -----------------------------------------------------------------------------
# Zugriff
# -----------------------------------------------------------------------------

# Zugriff via key
print (d2["key"])
print (d2[1])
print (d2[2])

# Zugriff mit verschiedenen Keys
d = {
    (1,2) : "tuple value",
    print : "ok",
    "pi"  : 3.14159,
    4711  : "Kölnisch Wasser"
}

print( d[(1,2)] )
print( d[print] )
print( d["pi"] )
print( d[4711] )


# -----------------------------------------------------------------------------
# Insert, Update, Merge, Delete
# -----------------------------------------------------------------------------

#  Neuer Wert zuweisen
d = {1: "H"}
d[1] = "Hello"
print(d)             # {1: 'Hello'}

# Neues Element hinzufügen
d[2] = "World"
print(d)             # {1: 'Hello', 2: 'World'}

# Update/Merge dict with other dictionary
dx = {2: "Tom", 3: "have a nice day"}
d.update(dx)         # Update existing entries, insert new entries
print(d)             # {1: 'Hello', 2: 'Tom', 3: 'have a nice day'}


# Wert löschen mit pop(key)
d.pop(3)
print(d)             # {1: 'Hello', 2: 'Tom'}

# -----------------------------------------------------------------------------
# Loops / Iterations
# -----------------------------------------------------------------------------

# Key, values, items:
d = {1:"v1", 2:"v2", 3:"v3"}
print(d.keys())     # dict_keys([1, 2, 3])
print(d.values())   # dict_values(['v1', 'v2', 'v3'])
print(d.items())    # dict_items([(1, 'v1'), (2, 'v2'), (3, 'v3')])

# Iiterations:
d = {1:"v1", 2:"v2", 3:"v3"}

for k in d:
    print(k, "=", d[k])


# Iterate over keys
for k in d.keys():
    print(k, "=", d[k])


# Iterate over values
for v in d.values():
    print(v)


# Iterate over items:
for k, v in d.items():
    print(k, "=", v)

# -----------------------------------------------------------------------------
# dict-comprehension

pairs = [("k1",11), ("k2", 22)]

d1 = {}
for k, v in pairs:
    d1[k] = v
print(d1)                           # {'k1': 11, 'k2': 22}

d2 = { k : v for k, v in pairs}
print(d2)                           # {'k1': 11, 'k2': 22}

# =============================================================================
# The end.
