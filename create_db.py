from market import app, db
from market.models import Item, User

user1 = User(username='toogni', email_address='contato.togni@gmail.com', password_hash='1234', budget=1000)
user2 = User(username='johndoe', email_address='johndoe@gmail.com', password_hash='1234')

item1 = Item(name='Iphone 10', price=850, barcode='852456952623', description='desc')
item2 = Item(name='Iphone 11', price=1000, barcode='525652145852', description='desc2')
item3 = Item(name='Laptop', price=420, barcode='158652456952', description='desc3')

with app.app_context():
  db.drop_all()
  db.create_all()

  db.session.add(user1)
  db.session.add(user2)
  
  db.session.add(item1)
  db.session.add(item2)
  db.session.add(item3)
  
  db.session.commit()

  item1.owner = User.query.filter_by(username='toogni').first().id

  db.session.add(item1)
  db.session.commit()

  print('Database created')