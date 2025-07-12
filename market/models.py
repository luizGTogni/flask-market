from market import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(length=30), nullable=False, unique=True)
  email_address = db.Column(db.String(length=50), nullable=False, unique=True)
  password_hash = db.Column(db.String(length=60), nullable=False)
  budget = db.Column(db.Integer(), nullable=False, default=0)
  items = db.relationship('Item', backref='owner_user', lazy=True)

  @property
  def prettier_budget(self):
     if len(str(self.budget)) >= 5 and len(str(self.budget)) < 7:
        return f'{int(self.budget / 1000)}K'
     
     if len(str(self.budget)) >= 7 and len(str(self.budget)) < 10:
        return f'{int(self.budget / 1000000)}M'
     
     if len(str(self.budget)) >= 10 and len(str(self.budget)) < 13:
        return f'{int(self.budget / 1000000000)}B'
     
     return f'{self.budget}$'

  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

  def check_password_correction(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)
  
  def can_purchase(self, item_price):
    return self.budget >= item_price
  
  def can_sell(self, item):
    return item in self.items

class Item(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique=True)
  barcode = db.Column(db.String(length=12), nullable=False, unique=True)
  price = db.Column(db.Integer(), nullable=False)
  description = db.Column(db.String(length=1024), nullable=False, unique=True)
  owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

  def __repr__(self):
        return f'Item {self.name}'
  
  def purchase(self, user):
    self.owner = user.id
    user.budget -= self.price
    db.session.commit()

  def sell(self, user):
    self.owner = None
    user.budget += self.price
    db.session.commit()