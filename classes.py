class Pizza:

    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(
            f'I would like a {self.size}-inch, {self.style} pizza with {" and ".join(self.toppings)}.')


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "deep dish"
meat_lovers.add_topping("pepperoni")
meat_lovers.add_topping("sausage")
meat_lovers.print_order()

kids = Pizza()
kids.size = 8
kids.style = "thin crust"
kids.add_topping("cheese")
kids.print_order()
