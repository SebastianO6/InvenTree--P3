from lib import CONN, CURSOR

class Items:
    def __init__(self, name, quantity, price, category = None, id = None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category 