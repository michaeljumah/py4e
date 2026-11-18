import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name, price, quantity=0):
        #run validations
        assert price >= 0
        assert quantity >= 0

        #asign to object self
        self.name = name
        self.price = price
        self.quantity = quantity

        #
        Item.all.append(self)


    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("phone", 1000, 7)

Item.instantiate_from_csv()


print(Item.all)