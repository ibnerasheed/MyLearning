from item import Item

"""Now see how inheritance work which will inherit item class methods and attributes.
so here broken_phones etc are new methods
"""


class Phone(Item):  # Inheriting class Item
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods.Super function allows
        # us tto have attribute access from parent classes
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
