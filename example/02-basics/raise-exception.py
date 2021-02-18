# =============================================================================
# Python examples - raise an exception
# =============================================================================

try:
    input = -1
    if input < 0:
        raise Exception("Number must by positive")
except Exception as e:
    print("Invalid input:", str(e))

# =============================================================================
# The end.