import time

class Item():

    count = 0

    def __init__(self, number):
        self.number = number
        print("Create item", self.number)
        Item.count += 1

    def __del__(self):
        print("Delete item", self.number)
        Item.count -= 1


print(Item.count)

item47 = Item(47)
print(Item.count)

item99 = Item(99)
print(Item.count)

del item47
print(Item.count)

print("Sleep 5 seconds...")
time.sleep(5)

