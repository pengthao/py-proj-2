from basic import app, db, Puppy
app.app_context().push()

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()


all_puppies = Puppy.query.all()
print(all_puppies)

puppy_one = db.session.get(Puppy, 1)
print(puppy_one)
puppy_three = db.session.get(Puppy, 3)
print(puppy_three)

puppy_frankie = Puppy.query.filter_by(name ='Frankie')
print(puppy_frankie.all())


first_puppy = db.session.get(Puppy, 1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
print(puppy_one)

second_pup = db.session.get(Puppy, 2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)