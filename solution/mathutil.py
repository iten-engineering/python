
class MathUtil:

    @staticmethod
    def min(a, b, c):
        if (a < b and a < c):
            return a
        elif b < c:
            return b
        return c

    @staticmethod
    def max(a, b, c):
        if (a > b and a > c):
            return a
        elif b > c:
            return b
        return c

if __name__ == '__main__':
    print("Das Maximum von 5,12,20 ist: " + str(MathUtil.max(5,12,20)))
    print("Das Minimum von 5,12,20 ist: " + str(MathUtil.min(5,12,20)))
    print("Das Maximum von 49,3,14 ist: " + str(MathUtil.max(49,3,14)))
    print("Das Minimum von 49,3,14 ist: " + str(MathUtil.min(49,3,14)))

