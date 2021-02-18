# =============================================================================
# Python examples - modules
# =============================================================================

# -----------------------------------------------------------------------------
# Module
# -----------------------------------------------------------------------------

# Module
# - Mit Python können Definitionen (Funktionen, Klassen) in eine eigenen Datei (Modul) ausgelagert werden.
# - Die Definitionen eines Moduls können in andere Modlue oder das Hauptprogramm importiert und dort genutzt werden
# - Der Datei Name entspricht dabei dem Modulnamen mit dem Suffix ".py"
# - Innerhalb vom Modul ist der Modulname via die interen Varialble "__name__" verfügbar

import fibo

print ("Fibo sample:")
fibo.print_fib(100)

result = fibo.fib(100)
print(result)

print(("Show module details:"))
print(dir(fibo))

# -----------------------------------------------------------------------------
# Import
# -----------------------------------------------------------------------------

# Sample: `import module `
# - imports everything and keeps it in the module's namespace
# - module.func()
# - module.className.func()

# Sample: `from module import *`
# - imports everything under the current namespace
# - func()
# - className.func()
# > not recommended

# Sample: `from module import className`
# - selectively imports under the current namespace
# - className.func()
# - like standard modules: math, os, sys

# -----------------------------------------------------------------------------
# Import with custom name
# -----------------------------------------------------------------------------

# game.py
# import the draw module
# if visual_mode:
#     # in visual mode, we draw using graphics
#     import draw_visual as draw
# else:
#     # in textual mode, we print out text
#     import draw_textual as draw
#
# def main():
#     result = play_game()
#     # this can either be visual or textual depending on visual_mode
#     draw.draw_game(result)

# -----------------------------------------------------------------------------
# Executing modules as scripts
# -----------------------------------------------------------------------------

# When you run a Python module with: python fibo.py <arguments>
# - the code in the module will be executed, just as if you imported it,
# - but with the __name__ set to "__main__".

# That means that by adding this code at the end of your module:
#     if __name__ == "__main__":
#         import sys
#         fib(int(sys.argv[1]))
# you can make the file usable as a script as well as an importable module,
# because the code that parses the command line only runs if the module is executed as the “main” file!


# -----------------------------------------------------------------------------
# Further details
# -----------------------------------------------------------------------------

# Links:
# - https://docs.python.org/3/tutorial/modules.html
# - https://realpython.com/python-modules-packages/

# =============================================================================
# The end.
