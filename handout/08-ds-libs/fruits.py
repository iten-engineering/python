
class Fruits:

    def __init__(self, apple, orange, banana):
        self.apple = apple
        self.orange = orange
        self.banana = banana

    def __str__(self):
        return "Apple={}, Orange={}, Banana={}".format(self.apple, self.orange, self.banana)    

    def __add__(self, other):
        if type(other) == int:
            apple = self.apple + other
            orange = self.orange + other
            banana = self.banana + other
        else:
            apple = self.apple + other.apple        
            orange = self.orange + other.orange        
            banana = self.banana + other.banana
        return Fruits(apple, orange, banana)        

    def add(self, other):
        apple = self.apple + other.apple        
        orange = self.orange + other.orange        
        banana = self.banana + other.banana
        return Fruits(apple, orange, banana)        

f1 = Fruits(1,2,3)
f2 = Fruits(10,20,30)

fx = f1 + f2
fy = f1.add(f2)

print(f1)
print(f2)
print(fx)
print(fy)
