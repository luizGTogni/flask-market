from market import app, db
from market.models import Item, User
from market.forms import RegisterForm
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = Item.query.all()

  return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()
  
  if form.validate_on_submit():
    user_to_crate = User(usename=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)

    db.session.add(user_to_crate)  
    db.session.commit()

    return redirect(url_for('market_page'))

  has_error = form.errors != {}
  if has_error:
    for err_msg in form.errors.values():
      print(f'There was an error with creating a user: {err_msg}')

  return render_template('register.html', form=form)