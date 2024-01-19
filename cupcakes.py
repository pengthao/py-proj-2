from pprint import pprint

class Cupcakes:
    def __init__(self, index, name, servings, cake, toppings, cost):
        self.index = index
        self.name = name
        self.servings = servings
        self.cake = cake
        self.toppings = toppings
        self.cost = cost
    
    def display_details(self):
        return f"{self.name} a {self.cake} flavored cupcake topped with {self.toppings}. {self.servings} servings for ${self.cost}."
    
    def to_dictionary(self):
        return {
            "index": self.index,
            "name": self.name,
            "servings": self.servings,
            "cake": self.cake,
            "toppings": self.toppings,
            "cost": self.cost
        }
    
    