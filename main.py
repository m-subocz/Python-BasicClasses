from typing import List


class Order:
    def __init__(self, total_cost: int, adress: str, items: List[str]) -> None:
        self.total_cost = total_cost
        self.adress = adress
        self.items = items

    def insert(self, x: str) -> List[str]:
        self.items.reverse()
        self.items.append(x)
        self.items.reverse()
        return self.items

    def __add__(self, other):
        total_cost = self.total_cost
        total_items = self.items
        if self.adress == other.adress:
            total_cost = self.total_cost + other.total_cost
            total_items = self.items + other.items
        return Order(self.adress, total_cost, total_items)


Order1: Order = Order(4002, 'London', ['item1', 'item2'])
Order2: Order = Order(2992, 'Oslo', ['item3'])
Order3: Order = Order(1243, 'London', ['item4'])
Order4: Order = Order(2544, 'London', ['item5', 'item6'])

Order5: Order = Order1.__add__(Order4)
Order6: Order = Order1.__add__(Order2)

print(Order5.total_cost, Order5.adress, Order5.items)
print(Order6.total_cost, Order6.adress, Order6.items)

print(Order1.total_cost, Order1.adress, Order1.items)
print(Order2.total_cost, Order2.adress, Order2.items)
print(Order3.total_cost, Order3.adress, Order3.items)
print(Order4.total_cost, Order4.adress, Order4.items)
