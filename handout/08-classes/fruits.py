
class FruitBasket:

    def __init__(self, apple, banana, orange):
        self.apple = apple
        self.banana = banana
        self.orange = orange

    def __str__(self):
        return f"apple={self.apple}, banana={self.banana}, orange={self.orange}"
    
    def __add__(self, other):
        if isinstance(other, int):
            apple = self.apple + other
            banana= self.banana + other
            orange= self.orange + other
        else:
            apple = self.apple + other.apple
            banana= self.banana + other.banana
            orange= self.orange + other.orange
        
        return FruitBasket(apple, banana, orange)

    def add(self, other):
        if isinstance(other, int):
            apple = self.apple + other
            banana= self.banana + other
            orange= self.orange + other
        else:
            apple = self.apple + other.apple
            banana= self.banana + other.banana
            orange= self.orange + other.orange
        
        return FruitBasket(apple, banana, orange)




basketA = FruitBasket(1,3,7)
basketB = FruitBasket(5,3,9)

basketC = basketA + basketB
basketD = basketA.add(basketB)

print(basketA)
print(basketB)
print(basketC)
print(basketD)

basketE = basketA + 5
print(basketE)