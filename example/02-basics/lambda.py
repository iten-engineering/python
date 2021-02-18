# =============================================================================
# Python examples - lambda
# =============================================================================

add = lambda a, b : a + b
print(add(1,2))

def multiplier(n):
    return lambda a : a * n

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

# =============================================================================
# The end.