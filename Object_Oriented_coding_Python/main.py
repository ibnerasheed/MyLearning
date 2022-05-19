""" Class allow data type of our own.Like below.So we will make Item datatype
   Creating an instance/object is same thing.
   Now __"  "__ is called magic methods in python
"""


class Item:
    def __init__(self, name, price, quantity = 0):
        print(f"An instance created : {name}")
        self.name = name #dynamic attribute assingment
        self.price = price
        self.quantity = quantity
    """
    Advantage of magic method innit:
    to save this from:
    item1.name = "Phone"
    item1.price = 100
    item1.quantity = 5
    Instead use the self. technique and avoid that.It also assurres dynamic nature of the code
    """

    """ make methods now.methods mean functions.Function inside classes are methods.
        Python dont allows to leave methods empty.
        dot "." sign is used to acess attributes of a class
    """

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone", 100, 5)


item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)



