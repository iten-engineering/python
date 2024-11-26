import time



class Item:

    instance_count = 0

    # constructor
    def __init__(self, number):
        self.number = number
        Item.instance_count += 1
        print(f"Create item {self.number}, total={Item.instance_count}")

    # destructor
    def __del__(self):
        Item.instance_count -= 1
        print(f"Delete item {self.number}, total={Item.instance_count}")


items = []
for i in range(0,10):
    item = Item(i)
    items.append(item)

time.sleep(3)



