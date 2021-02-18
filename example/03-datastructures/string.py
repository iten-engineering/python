# =============================================================================
# Python examples - strings
# =============================================================================

# -----------------------------------------------------------------------------
# Declarations
# -----------------------------------------------------------------------------
quote = '"Titanic" is a cool movie.'
doublequote = "'Titanic' is a cool movie"
escape = 'I\'m hungry'
multilines = """This is going
over multiples lines"""

path = "c:\\tmp"
rawpath = r"c:\tmp"             # Raw String - Escape Sequenzen werden ignoriert
unicode = '\U000000e4'          # ä (ab Python 3, wird direkt als Unicode interpretiert)
unicodePython2 = u'\U000000e4'  # ä (Schreibweise bei Python 2)

# -----------------------------------------------------------------------------
# capitalize
# -----------------------------------------------------------------------------

s = "this is a test"
print(s.capitalize())                                           # This is a test

# -----------------------------------------------------------------------------
# format
# -----------------------------------------------------------------------------

name = "Tom"
s = "Hello {}".format(name)                                     # Hello Tom
print(s)

s = "i have {} {}".format(1,"cat")                              # i have 1 cat
print(s)
s = "i have {1} {0}".format("cat",1)                            # i have 1 cat
print(s)
s = "i have {count} {animal}".format(count=1, animal="cat")     # i have 1 cat
print(s)

# -----------------------------------------------------------------------------
# format numbers
# -----------------------------------------------------------------------------

import math
pi = math.pi

# {:breite.genauigkeit}
s = "pi={:.2}".format(pi)
print("[", s, "]", sep="")
s = "pi={:10.2}".format(pi)
print("[", s, "]", sep="")

# {ausrichtung:breite.genauigkeit}
s = "pi={:>10.2}".format(pi)        # rechts
print("[", s, "]", sep="")
s = "pi={:<10.2}".format(pi)        # links
print("[", s, "]", sep="")
s = "pi={:^10.2}".format(pi)        # centriert
print("[", s, "]", sep="")

# {füllung=:breite.genauigkeit}
s = "pi={:0=10.2}".format(pi)
print("[", s, "]", sep="")

# -----------------------------------------------------------------------------
# find, rfind, replace, starts/endswith, in
# - s.find() gibt erste Position (Index) zurück, wo man element in s findet. Das ist das selbe wie die index Methode.
# - s.rfind(element) gibt die letzte Position zurück wo man element in s findet
# -----------------------------------------------------------------------------

text = "this and that"
text.find("th")       # 0
text.rfind("th")      # 9

s = "Fall is coming".replace("Fall", "Winter")   # Winter is coming

s.startswith("Winter")                           # True
s.startswith("Fall")                             # False

s.endswith("coming")                            # True
s.endswith("leaving")                           # False

"test" in "this is a test"                       # True
"x" in "abc"                                     # False

# -----------------------------------------------------------------------------
# split, join
# -----------------------------------------------------------------------------

text = "Hello Tom, how are you"
tokens = text.split()                      # ["Hello", "Tom,", "how", "are", "you"]
print(tokens)
tokens = text.split(",")                   # ["Hello Tom", "how are you"]
print(tokens)

num = 15.75
before, after = str(num).split(".")
print(before, ":", after)

# -----------------------------------------------------------------------------
# strip, lstrip, rstrip
# -----------------------------------------------------------------------------

"  some text   ".strip()            # "some text"
"__some text___".strip("_")         # "some text"
"  some text   ".lstrip()           # "some text  "
"  some text   ".rstrip()           # "  some text"

# -----------------------------------------------------------------------------
# ljust, center, rjust
# -----------------------------------------------------------------------------

s = "expand text".ljust(20)
print("[", s, "]", sep="")        # [expand text         ]

s = "expand text".rjust(20)
print("[", s, "]", sep="")        # [         expand text]

s = "expand text".center(20)
print("[", s, "]", sep="")        # [    expand text     ]

# =============================================================================
# The end.
