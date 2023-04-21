
class Calculator:

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y == 0:
            raise Exception("Divison durch 0 ist nicht erlaubt")
        return x / y            