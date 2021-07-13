#imnport required packages
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_migrate import Migrate

#create model that'll be table in database
db = SQLAlchemy()

#define a model
#parents: inheriting behavior from SQL alchemy class
#we need this to tell comp that we're making a model
class Animal(db.Model):
    #similar to CREATE table quereys col/attributes to go into this model
    #variable = 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True) #not allowed to have no value
    height = db.Column(db.Integer, nullable=True, default='Unknown')
    weight = db.Column(db .Integer, nullable=True, default='Unknown')
    climate = db.Column(db.String(50), nullable=True, default='all climates')
    reigon = db.Column(db.String(50))
#repr has specific use, to give dev more info
    def __repr__(self):
        return f"<Animal: {self.name}"


