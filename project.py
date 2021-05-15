from flask import Flask ,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy 
from database_setup import db , Restaurant , MenuItem

app = Flask(__name__)   
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
db.init_app(app)
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html',restaurant = restaurant , items = items)
    
# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/',methods= ['GET','POST'])
def newMenuItem(restaurant_id):
    if request.method == "POST":
        #new =MenuItem(name = request.form['name'],id = 0,description = '',price ='',course = ' ',restaurant_id = restaurant_id)
        new =MenuItem(name = request.form['name'],restaurant_id = restaurant_id)
        db.session.add(new)
        db.session.commit()
        flash('Created successfully ')
        return redirect( url_for('restaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('newMenuItem.html',restaurant_id = restaurant_id)

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods= ['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    update = db.session.query(MenuItem).filter_by(id = menu_id)#.one()
    if request.method == "POST":
        update.name =  request.form['name']
        db.session.add(update)
        db.session.commit()
        flash('Edited successfully ')
        return redirect( url_for('restaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('editMenuItem.html',restaurant_id = restaurant_id,menu_id = menu_id)
# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/',methods= ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    Delete = db.session.query(MenuItem).filter_by(id = menu_id)#.one()
    if request.method == "POST":
        db.session.delete(Delete)
        db.session.commit()
        flash('Deleted successfully ')
        return redirect( url_for('restaurantMenu',restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html',restaurant_id = restaurant_id,menu_id = menu_id)
if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.55', port=5000)

