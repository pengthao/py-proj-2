
from abc import ABC, abstractmethod

class Cupcake(ABC):


    def __init__(self, size,name,price,flavor,frosting,sprinkles,filling, description):
        
        self.size = size
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling
        self.description = description

    def display_details(self):
        return f"""
                Cupcake: {self.name}
                Size: {self.size}
                Price: {self.price}
                Flavor: {self.flavor}
                Frosting: {self.frosting}
                Sprinkles: {self.sprinkles}
                Filling: {self.filling}
                Description: {self.description}
                """
    
    def add_sprinkles(self, sprinkles):
        for sprinkle in sprinkles:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, amount):
        return amount * self.price
    
class Mini(Cupcake):
    size = "mini"

    def mini_price(self, amount):
        multiplier = .8
        return amount * self.price * multiplier


##if on the order page the size selection is mini
##then change the class of object to mini and apply multiplier 
##at checkout