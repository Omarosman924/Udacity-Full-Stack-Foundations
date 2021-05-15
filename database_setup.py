
from flask import Flask ,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'

db = SQLAlchemy(app)
class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(250), nullable=False)
    # def __init__(self,id,name):
    #     self.id = id 
    #     self.name = name

class MenuItem(db.Model):
    __tablename__ = 'menu_item'
    name =db.Column(db.String(80), nullable = False)
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    # def __init__(self,name,id,description,price,course,restaurant_id):
    #     self.name =name
    #     self.id = id
    #     self.description = description
    #     self.price = price
    #     self.course = course
    #     self.restaurant_id = restaurant_id

try:
    db.create_all()
except:
    pass