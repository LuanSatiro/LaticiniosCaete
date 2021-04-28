from app import db
from flask_login import UserMixin
from datetime import datetime


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username =  db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    contato = db.Column(db.String(60))
    city = db.Column(db.String(60))
    street = db.Column(db.String(60))
    number = db.Column(db.Integer)

class Order(db.Model):
   __tablename__ = "order"
   id = db.Column(db.Integer, primary_key=True, nullable=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE', onupdate='CASCADE'))
   units = db.Column(db.Integer)
   date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now)
   status = db.Column(db.String(60))

class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(30))
    img = db.Column(db.String(60))
    prices= db.Column(db.Float)
    relation = db.relationship(Order, backref="products", passive_deletes=True, passive_updates=True)
    

    
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


 

