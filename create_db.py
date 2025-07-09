from market import app, db
from market.models import Item

item1 = Item(name='Iphone 10', price=850, barcode='852456952623', description='desc')
item2 = Item(name='Iphone 11', price=1000, barcode='525652145852', description='desc2')
item3 = Item(name='Laptop', price=420, barcode='158652456952', description='desc3')

with app.app_context():
  db.create_all()

  db.session.add(item1)
  db.session.add(item2)
  db.session.add(item3)
  
  db.session.commit()