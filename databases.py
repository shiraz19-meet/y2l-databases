from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(description,price,color,rating):
    product_object = Product(
        description=description,
        price=price,
        color=color,
        rating=rating)
    session.add(product_object)
    session.commit()


def update_product(rating, price):
    product_object = session.query(
        Product).filter_by(
        price=price,
        description=description).first()
    product_object.rating = rating
    session.commit()

  pass

def delete_product(id):
    session.query(Product).filter_by(
       id=id).delete()
    session.commit()



def get_product(id):
  pass
