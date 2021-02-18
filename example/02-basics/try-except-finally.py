# =============================================================================
# Python examples - try except finally
# =============================================================================

def divide(x, y):
    success = True
    try:
        result = x / y
    except ZeroDivisionError:
        success = False
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        if (success):
            print("> divison successfully done")
        else:
            print("> division failed")

divide(10,2)
divide(10,0)
divide(10,5)

# =============================================================================
# The end.