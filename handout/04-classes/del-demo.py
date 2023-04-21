class Item:

    # constructor
    def __init__(self, number):
        self.number = number
        print("Create item:", self.number)

    # destructor
    def __del__(self):
        print("Delete item:", self.number)

# create instance
item = Item(47)
item2= Item(2)

# delete instance
del item