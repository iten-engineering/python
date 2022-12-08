
class Fruits:

    def __init__(self, apple, orange):
        self.apple = apple
        self.orange = orange

    def __add__(self, other):
        apple = self.apple + other.apple
        orange = self.orange + other.orange
        return Fruits(apple, orange)

    def add_to_exiting(self, other):
        self.apple = self.apple + other.apple
        self.orange = self.orange + other.orange
        return self



if __name__ == '__main__':
    f1 = Fruits(1,1)
    f2 = Fruits(2,4)
    f1.add_to_exiting(f2)
    print(f1.apple, f1.orange)

