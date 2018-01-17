from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)




#foursquare_client_id = ''

#foursquare_client_secret = ''

#google_api_key = ''

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
    if request.method == 'GET':
        #Call the method to Get all of the restaurants
        return "Get all restaurant"
    elif request.method == 'POST':
        #Call the method to make a new restaurant
        return "Make a restaurant"


@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
    if request.method == 'GET':
        #Call the method to get a restaurant
        return "Get one restaurant"
    elif request.method == 'POST':
        #Call the method to edit a restaurant
        return "Edit a restaurant"
    elif request.method == 'DELETE':
        #Call the method to delete a restaurant
        return "Delete a restaurant"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
