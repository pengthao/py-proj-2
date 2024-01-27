from basic import app, db, Puppy

app.app_context().push()
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie',4)

db.session.add(sam)
db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank)