from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = [
    { 'id': 1, 'name': 'Phone', 'barcode': '893524418515', 'price': 500 },
    { 'id': 2, 'name': 'Laptop', 'barcode': '125485245256', 'price': 900 },
    { 'id': 3, 'name': 'Keyboard', 'barcode': '854226555545', 'price': 150 }
  ]

  return render_template('market.html', items=items)