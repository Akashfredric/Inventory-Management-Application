from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/test-withtwodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our  database
class Product_Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.String(100))
    to_loc = db.Column(db.String(100))
    from_loc = db.Column(db.String(100))
    product_quantity = db.Column(db.String(100))
    date_time = db.Column(db.String(100))
    
    def __init__(self,product_id, from_loc, to_loc,product_quantity,date_time):
        self.product_id = product_id
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.product_quantity = product_quantity
        self.date_time = date_time


        

@app.route('/')
def Index():

    all_data = Product_Data.query.all()
    return render_template("index.html", products = all_data)



@app.route('/insert' ,methods=['POST'])
def insert():
    if request.method == 'POST':
        product_id = request.form['Product ID']
        from_loc = request.form['From Location']
        to_loc = request.form['To Location']
        product_quantity = request.form['Quantity']
        date_time= request.form['datetime']
        

        my_data = Product_Data(product_id,from_loc,to_loc,product_quantity,date_time)
        db.session.add(my_data)
        db.session.commit()

        flash("Product details Inserted Successfully")

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Product_Data.query.get(request.form.get('id'))
 
        my_data.product_id = request.form['Product ID']
        my_data.from_loc = request.form['From Location']
        my_data.to_loc = request.form['To Location']
        my_data.product_quantity = request.form['Quantity']
        my_data.date_time = request.form['datetime']
        
 
        db.session.commit()
        flash("Product details Updated Successfully")
 
        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Product_Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Product info Deleted Successfully")
 
    return redirect(url_for('Index'))



if __name__ == "__main__":

    app.run(debug=True)