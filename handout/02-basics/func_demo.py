
def hello(name, greeting="Hello", action=None):
    print(greeting, name)
    if action is not None:
        print(action)


hello("Sam")
hello("Anna", greeting="Dear")
hello("James", action="Sell my car")

hello("James", "test2")

