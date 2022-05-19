""" Class allow data type of our own.Like below.So we will make Item datatype
   Creating an instance/object is same thing.
   Now __"  "__ is called magic methods in python
"""
import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount. This is global in nature
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments.Using assert you can add exception statements.
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign to self object
        self.__name = name # double __ makes the attribute inaccessible like private thing in oops
        self.price = price
        self.quantity = quantity

        # Assign to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    """
    Advantage of magic method innit:
    to save this from:
    item1.name = "Phone"
    item1.price = 100
    item1.quantity = 5
    Instead use the self. technique and avoid that.It also assures dynamic nature of the code.
    Also check name :str and price:float is being done so that if someone by mistake make a class using 
    other data type,errors can be avoided. So,it's a best practice to do such stuffs.

    Class attribute: Attribute that belongs to class.Till above we have done instance attribute only.Class
    attribute can be access by instance level too.
    """

    """ make methods now.methods mean functions.Function inside classes are methods.
        Python don't allows to leave methods empty.
        dot "." sign is used to access attributes of a class
    """

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):  # static method.with static method we never send object as first parmeter
        # We will find out the floats that are point zero
        # For eg :5.0, 10.0
        if isinstance(num, float):
            # Count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def apply_discount(self):
        self.price = self.price * self.pay_rate


print(Item.is_integer(7))

# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)


# print(item1.pay_rate) .Bringing attribute from class level when it dosen't find in instance level.

# print(Item.__dict__) # shows all the attributes for Class level
# print(item1.__dict__)


# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
