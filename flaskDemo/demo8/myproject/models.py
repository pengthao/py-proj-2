#set up db inside the __init__.py under myproject
from myproject import db

class Puppy(db.Model):

    __tablename__='puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref ='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"ID:{self.id}:Puppy's name is {self.name} and owner is {self.owner.name}."
        else:
            return f"ID:{self.id}:Puppy name is {self.name} and has no owner yet."


class Owner(db.Model):

    __tablename__='owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.puppy_id = pup_id
        
    def __repr__(self):
        return f"Owner Name: {self.name}"




'''   
def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):

    __tablename__='toys'
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__ (self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id'''