import os
from abc import ABC, abstractmethod
import csv

class Cupcake(ABC):

    def __init__(self, id, img, size, name, price, flavor, frosting, sprinkles, filling, description):
        
        self.id = id
        self.img = img
        self.size = size
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = sprinkles
        self.filling = filling
        self.description = description

    
    def to_dictionary(self):
        
        return {
            'id':self.id,
            'img': self.img,
            'size': self.size,
            'name': self.name,
            'price': self.price,
            'flavor': self.flavor,
            'frosting': self.frosting,
            'sprinkles': self.sprinkles,
            'filling': self.filling,
            'description': self.description
        }
    @classmethod
    def from_dict(cls, cupcake_dict):
        return cls(
            id=cupcake_dict['id'],
            img=cupcake_dict['img'],
            size=cupcake_dict['size'],
            name=cupcake_dict['name'],
            price=cupcake_dict['price'],
            flavor=cupcake_dict['flavor'],
            frosting=cupcake_dict['frosting'],
            sprinkles=cupcake_dict['sprinkles'],
            filling=cupcake_dict['filling'],
            description=cupcake_dict['description']
        )

    def display_img(self):
        return self.img
    
    def display_list(self):
        return f"Cupcake: {self.name}\nFrom ${self.price}"


    def display_details(self):
        return f"""
            Cupcake: {self.name}\n
            Size: {self.size}\n
            Price Per Cupcake: {self.price}\n
            Flavor: {self.flavor}\n
            Frosting: {self.frosting}\n
            Sprinkles: {self.sprinkles}\n
            Filling: {self.filling}\n
            Description: {self.description}
        """
    
    def add_sprinkles(self, sprinkles):
        for sprinkle in sprinkles:
            self.sprinkles.append(sprinkle)

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
    

class User():
    def __init__ (self, name, phone, paymentInfo):

        self.name = name
        self.phone = phone
        self.paymentInfo = paymentInfo #dicitonary card type: visa,cardNum: 123234


class Order():
    def __init__ (self, uName, paymentInfo, orderDate, pickupDate, cupcakes):

        self.uName = uName
        self.paymentInfo = paymentInfo
        self.orderDate = orderDate
        self.pickupDate = pickupDate
        self.cupcakes = cupcakes
        self.pickedUp = False

    def pickedUp(self):
        self.pickedUp = True




def cupcakes_list():
    cupcake_list = []
    file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
    with open(file_path) as csvfile:
        for line in csvfile:
            if isinstance(line, str):
                values = line.strip().split(", ")

            id = values[0] if len(values) > 0 else None
            image = values[1] if len(values) > 1 else None
            size = values[2] if len(values) > 2 else None
            name = values[3] if len(values) > 3 else None
            try:
                # Attempt to convert the 'price' value to a float
                price = float(values[4]) if len(values) > 4 else 0.0
            except ValueError:
                # Handle the ValueError (e.g., print a message and set price to 0.0)
                print(f"Error converting 'price' to float. Line: {line}")
                price = 0.0
            flavor = values[5] if len(values) > 5 else None
            frosting = values[6] if len(values) > 6 else None
            sprinkles = values[7] if len(values) > 7 else None
            filling = values[8] if len(values) > 8 else None
            description = values[9] if len(values) > 9 else 'None'

            try:
                cupcake = Cupcake(
                    id=int(id),
                    img=image,
                    size=size,
                    name=name,
                    price=float(price),
                    flavor=flavor,
                    frosting=frosting,
                    sprinkles=sprinkles,
                    filling=filling,
                    description=description
                )
                if not cupcake.id in [c.id for c in cupcake_list]:
                    cupcake_list.append(cupcake)
            except ValueError:
                print(f"Error processing line: {line}")

    return cupcake_list

def write_cupcakes(cupcakes):
    file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
    with open(file_path, mode='w', newline='') as csvfile:
        for cupcake in cupcakes:
            id = cupcake.id if cupcake.id else None
            img = cupcake.img if cupcake.img else "http://tinyurl.com/muz2sr2y"
            size = cupcake.size if cupcake.size else "n/a"
            name = cupcake.name if cupcake.name else "n/a"
            price = cupcake.price if cupcake.price else "n/a"
            flavor = cupcake.flavor if cupcake.flavor else "n/a"
            sprinkles = str(cupcake.sprinkles) if cupcake.sprinkles else "n/a"
            filling = cupcake.filling if cupcake.filling else "n/a"
            description = cupcake.description if cupcake.description else "n/a"

            csvfile.write(f"{id},{img},{size},{name},{price},{flavor},{sprinkles},{filling},{description}\n")


def read_shoppingCart():
    cart = []
    file_path = os.path.join(os.path.dirname(__file__), "cart.csv")

    with open(file_path) as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            print(f"Processing line: {line}")

            try:
                id = line[0]
                image = line[1]
                size = line[2]
                name = line[3]
                price = float(line[4])
                flavor = line[5]
                frosting = line[6]
                sprinkles = line[7]
                filling = line[8]
                description = line[9]
                quantity = int(line[10])

                print(f"Extracted values: id={id}, image={image}, size={size}, name={name}, price={price}, flavor={flavor}, frosting={frosting}, sprinkles={sprinkles}, filling={filling}, description={description}, quantity={quantity}")

                cupcake = dict(
                    id=int(id),
                    img=image,
                    size=size,
                    name=name,
                    price=price,
                    flavor=flavor,
                    frosting=frosting,
                    sprinkles=sprinkles,
                    filling=filling,
                    description=description,
                    quantity=quantity
                )
                cart.append(cupcake)
            except Exception as e:
                print(f"Error processing line: {line}")
                print(f"Error details: {e}")

    return cart

def write_shoppingCart(cupcakes):
    file_path = os.path.join(os.path.dirname(__file__), "cart.csv")

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        if not file_exists:
            # Write the header only if the file is being created for the first time
            csv_writer.writerow(['id', 'img', 'size', 'name', 'price', 'flavor', 'sprinkles', 'filling', 'description', 'quantity'])

        for cupcake in cupcakes:
            id = cupcake.get('id', "n/a")
            img = cupcake.get('img', "http://tinyurl.com/muz2sr2y")
            size = cupcake.get('size', "n/a")
            name = cupcake.get('name', "n/a")
            price = cupcake.get('price', 0)
            flavor = cupcake.get('flavor', "n/a")
            frosting = cupcake.get('frosting', "n/a")
            sprinkles = str(cupcake.get('sprinkles', "n/a"))
            filling = cupcake.get('filling', "n/a")
            description = cupcake.get('description', "n/a")
            quantity = cupcake.get('quantity', 0)

            # Write data
            csv_writer.writerow([id, img, size, name, price, flavor, frosting, sprinkles, filling, description, quantity])


def get_last_order_number():
    file_path = os.path.join(os.path.dirname(__file__), "order.csv")

    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip the header row
        next(csv_reader, None)
        # Check the last order number
        last_row = None
        for row in csv_reader:
            last_row = row
        if last_row:
            return int(last_row[0]) + 1
        else:
            return 1


def read_orders(order):
    file_path = os.path.join(os.path.dirname(__file__), "order.csv")

    

    with open(file_path) as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            print(f"Processing line: {line}")




def write_order(order_data):
    order_number = get_last_order_number()

    file_path = os.path.join(os.path.dirname(__file__), "order.csv")
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        if not file_exists:
            # Write the header only if the file is being created for the first time
            csv_writer.writerow(['order_number', 'name', 'phone', 'date', 'total'])

        # Write order data with the order number
        csv_writer.writerow([order_number, order_data['name'], order_data['phone'], order_data['date'], order_data['total']])

        # Write shopping cart data
        csv_writer.writerow(['id', 'img', 'size', 'name', 'price', 'flavor', 'sprinkles', 'filling', 'description', 'quantity'])
        for cupcake in order_data['shoppingCart']:
            csv_writer.writerow([
                cupcake.get('id', "n/a"),
                cupcake.get('img', "http://tinyurl.com/muz2sr2y"),
                cupcake.get('size', "n/a"),
                cupcake.get('name', "n/a"),
                cupcake.get('price', 0),
                cupcake.get('flavor', "n/a"),
                str(cupcake.get('sprinkles', "n/a")),
                cupcake.get('filling', "n/a"),
                cupcake.get('description', "n/a"),
                cupcake.get('quantity', 0)
            ])