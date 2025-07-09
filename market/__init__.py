from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
db = SQLAlchemy(app)

from market import routes