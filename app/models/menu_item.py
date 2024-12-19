from . import db

class MenuItem(db.Model):
    __tablename__  = 'menu_items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    price = db.Column(db.Float, nullable=False)