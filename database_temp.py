
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'

db = SQLAlchemy(app)
class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(250), nullable=False)
    def __init__(self,id,name):
        self.id = id 
        self.name = name

class MenuItem(db.Model):

    name =db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    restaurant = db.relationship(Restaurant) 

try:
    db.create_all()
except:
    pass