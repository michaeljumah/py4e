class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity=0):
        #asign to object self
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("phone", 1000, 7)
item1.apply_discount()
print(f'price:', item1.price)

print(f'total price', item1.calc_total_price())