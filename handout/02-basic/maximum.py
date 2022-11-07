
def max(v1, v2, v3=None):
    if v3 == None:
        if v1 > v2:
            return v1
        else: 
            return v2
    else:
        if v1 > v2 and v1 > v3:
            return v1
        elif v2 > v3:
            return v2
        return v3

print( max(3,9) )
print( max(30,90,15) )