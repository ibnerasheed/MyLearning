# When to use class methods and to use static methods?
class Item:
    @staticmethod
    def is_integer():
        """
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        """
        