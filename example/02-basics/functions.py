# =============================================================================
# Python examples - functions
# =============================================================================

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

def hello():
    print("Hello")

def greeting(name):
    print("Hello", name)

def weekend_greeting(name, greeting):
    print("Hello %s, i wish you %s"%(name, greeting))

hello()
greeting("Tom")
weekend_greeting("Zoé", "a nice weekend")

# -----------------------------------------------------------------------------
# Functions with Return
# -----------------------------------------------------------------------------

def add(a, b):
    return a + b

def mean(values):
    return sum(values) / len(values)

res = add(3,9)
print ("add(3,9) =", res)

res = mean([4,8,12])
print ("mean([4,8,12]) =", res)

# -----------------------------------------------------------------------------
# Arguments and defaults values
# -----------------------------------------------------------------------------

# Positional arguments sind obligatorisch und werden durch ihre Position gemapped:
def f1(arg1, arg2, arg3):
    print("f1: arg1={}, arg2={}, arg3={}".format(arg1,arg2,arg3))


# Keyword arguments sind fakultativ und werden durch ihre Position oder key gemapped:
def f2(arg1=None, arg2=10, arg3="Default"):
    print("f2: arg1={}, arg2={}, arg3={}".format(arg1,arg2,arg3))

# Mixed arguments:
# - Zuerst werden alle Argumente die die Funktion ohne key bekommen hat durch ihre Position gemapped
# - Dann werden die Restlichen durch ihre key gemapped
def f3(arg1, arg2, arg3="Default", arg4=99):
    print("f3: arg1={}, arg2={}, arg3={}, arg4={}".format(arg1,arg2,arg3,arg4))

f1(1,2,3)
f2()
f2(arg2=22)
f3(1,2)
f3(1,2, arg4=88)

# -----------------------------------------------------------------------------
# Unpack elements
# **args and **kwargs
# - *list unpacks the elements from list
# - **dict unpacks the items from dict
# -----------------------------------------------------------------------------

def f4(a, b, c=None, d=None):
    print("f4: a={}, b={}, c={}, d={}".format(a,b,c,d))

# Unpack elements from a list
f4(*[1,2])                   # a=1, b=2, c=None, d=None
f4(*[1,2], d=4)              # a=1, b=2, c=None, d=4

# Unpack elements from a dict
f4(1, 2, **{"c":3, "d":4})   # a=1, b=2, c=3, d=4
f4(1, 2, **{"d":4, "c":3})   # a=1, b=2, c=3, d=4


# -----------------------------------------------------------------------------
# Definitions with * and ** Syntax:
# - Konventionell braucht man *args und **kwargs
# - Alle zusätzlichen `positional` arguments werden in args gepackt
# - Alle zusätzlichen `keyword` arguments werden in kwarg gepackt
# -----------------------------------------------------------------------------

def f5(a, *args, k=9, **kwargs):
    print("f5: a={}, args={}, k={}, kwargs={}".format(a,args,k,kwargs))

f5(1)
f5(1,2,4,6,k=7,x=9,y=11)

# =============================================================================
# The end.