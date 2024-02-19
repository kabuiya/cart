class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_items(self, item_name, quantity, price):
        if item_name in self.items:
            self.total += quantity * price
            self.items[item_name] += quantity
            self.total += price * quantity
        else:
            self.total += price * quantity
            new_item = {item_name: quantity}
            self.items.update(new_item)
        print('ITEMS:', self.items, 'TOTAL:', self.total)

    def remove_item(self, item_name, quantity, price):
        if item_name in self.items:
            quantity_in_cart = self.items[item_name]
            if quantity >= quantity_in_cart:
                cost_to_remove = quantity_in_cart * price
                self.total -= cost_to_remove
                self.items.pop(item_name)
            else:
                self.items[item_name] -= quantity
                self.total -= price * quantity
        else:
            print('item not in shopping cart')
        print('total:', self.total, 'purchase_items:', self.items)

    def checkout(self, cash_paid):
        if cash_paid >= self.total:
            bal = cash_paid - self.total
            return bal
        else:
            return 'Cash not enough'


class Shop(ShoppingCart):
    def __init__(self):
        super().__init__()
        self.quantity = 100

    def remove_item(self, item_name, quantity, price):
        super().remove_item(item_name, quantity, price)
        return self.quantity - 1


cart1 = ShoppingCart()
cart1.add_items('drinks', 10, 10)
cart1.add_items('veg', 10, 10)
cart1.remove_item('veg', 15, 10)
s1 = Shop()
print(s1.remove_item('drink', 10, 10))

