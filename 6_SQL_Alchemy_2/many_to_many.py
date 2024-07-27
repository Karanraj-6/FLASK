from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///shop_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
           
db=SQLAlchemy(app)           

#association table
Customer_Product=db.Table(
    db.Colomn("customer_id",db.Integer,db.ForiengnKey("customer.id")),
    db.Colomn("product_id",db.Integer,db.ForiengnKey("product.id"))
)


class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(20), nullable=False, unique=True)
    items=db.relationship("Product", backref="owners",secondary=Customer_Product)
    
    def __repr__(self):
        return f"Customer('{self.name}','{self.email}')"

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product=db.Column(db.String(20), nullable=False)
    price=db.Column(db.Integer,nullable=False)
    
    def __repr__(self):
        return f"Product('{self.product}','{self.price}')"

if __name__ == "__main__":
    app.run(debug=True)
