# =============================================================================
# Python examples - standard libraries sys & subprocess
# =============================================================================

import sys
print(dir(sys))

print(sys.argv)         # Ausgabe aller Argumente [...]
print(sys.argv[0])      # Erstes Argument ist der Programm Name

print(sys.executable)   # Ausgabe absoluter Pfad zum Python Interpreter

print(sys.platform)     # Ausgabe der Plattform (z.B. win32)



print("----------------------------------------------------------------------")
print("sys.path:")
print("----------------------------------------------------------------------")

print(sys.path)

print("----------------------------------------------------------------------")
print("sys.modules:")
print("----------------------------------------------------------------------")

print(sys.modules)

print("----------------------------------------------------------------------")

sys.exit(0)

# -----------------------------------------------------------------------------
# Further details
# -----------------------------------------------------------------------------

# Links:
# - https://www.tutorialsteacher.com/python/sys-module

# =============================================================================
# The end.

