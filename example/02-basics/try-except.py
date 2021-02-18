# =============================================================================
# Python examples - try except
# =============================================================================

try:
    input = "12x"
    nr = int(input)
except:
    print("Invalid input: ", input)

# -----------------------------------------------------------------------------

try:
    input = "12x"
    nr = int(input)
except Exception as e:
    print("Invalid input: ", str(e) )

# -----------------------------------------------------------------------------

try:
    input = "12x"
    nr = int(input)
except Exception as e:
    print("Invalid input: ", str(e) )
finally:
    print("The 'try except' is finished")

# -----------------------------------------------------------------------------

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except (RuntimeError, TypeError, NameError):
    print("Catch all other expected errors.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# =============================================================================
# The end.