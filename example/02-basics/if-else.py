# =============================================================================
# Python examples - if else
# =============================================================================

seq = [1,2,3]

if len(seq) == 0:
    print("sequence is empty")
elif len(seq) == 1:
    print("sequence contains one element")
else:
    print("sequence contains several elements")

# -----------------------------------------------------------------------------
# If shorthand (Ternary operator)
# -----------------------------------------------------------------------------

a = 5
b = 3
x = 10 if a > b else 1        # better readable
y = a > b and 10 or 1         # style more like java or other languages
print(x)
print(y)

# =============================================================================
# The end.