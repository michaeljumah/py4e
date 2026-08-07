class Item:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_total_price(self):
        return self.price * self.quantity

item1 = Item("phone", 1000, 7)

print(item1.calc_total_price())