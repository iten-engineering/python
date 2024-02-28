

class Fruits:
    def __init__(self, apples, bananas, apricots):
        self.apples = apples
        self.bananas = bananas
        self.apricots = apricots

    def __add__(self, other):
        apples = self.apples + other.apples
        bananas= self.bananas + other.bananas
        apricots= self.apricots + other.apricots
        return Fruits(apples, bananas, apricots)
    
    def add(self, other):
        apples = self.apples + other.apples
        bananas= self.bananas + other.bananas
        apricots= self.apricots + other.apricots
        return Fruits(apples, bananas, apricots)


    def print(self):
        print("apples={}, bananas={}, apircots={}".format(self.apples,self.bananas, self.apricots))

if __name__ == "__main__":
    f1 = Fruits(1,1,1)
    f2 = Fruits(2,2,2)
    f3 = f1 + f2
    f3.print()
    f4 = f1.add(f2)
    f4.print()