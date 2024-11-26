
class FruitBasket:

    def __init__(self, ananas, banana, kiwi):
        self.ananas = ananas
        self.banana = banana
        self.kiwi = kiwi

    def __str__(self):
        return f"ananas={self.ananas}, banana={self.banana}, kiwi={self.kiwi}"
        
    def __add__(self, other):
        ananas = self.ananas + other.ananas
        banana = self.banana + other.banana
        kiwi = self.kiwi + other.kiwi
        return FruitBasket(ananas, banana, kiwi)

    def add(self, other):
        ananas = self.ananas + other.ananas
        banana = self.banana + other.banana
        kiwi = self.kiwi + other.kiwi
        return FruitBasket(ananas, banana, kiwi)

basketA = FruitBasket(1,5,9)
basketB = FruitBasket(3,7,1)

print(basketA)
print(basketB)

basketC = basketA + basketB
print(basketC)

basketD = basketA.add(basketB)
print(basketD)
