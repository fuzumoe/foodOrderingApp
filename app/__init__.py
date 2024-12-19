import os
from flask import Flask  
from flask_migrate import Migrate
from flask_restx import Api
from dotenv import load_dotenv
from .models import db
from .routes import register_routes

# Load environmental variables
load_dotenv()


""" 
 1. database interaction
 2. routs REST API
 3. TEMPLATES "html"
 4. STATIC FILES "js, css..."

"""
def create_app():
    # Initialize flask app
    app = Flask(__name__)
    
    
    # Configure MYSQL database using .env variables
    #{"DEV_DATABASE_URI":"mysql+mysqlconnector://root:top!secret@localhost/food_ordering"}
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEV_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Initialize extensions
    # initializes databases
    db.init_app(app)
    
    # creates all the tables by reading the model classes found under the model dir
    Migrate(app, db)
    
    # Initialize Flask-RESTx Api # for swagger ui
    
    app_version = os.getenv("FOOD_ORDERING_APP_VERSION", "1.0")
    app_title = os.getenv("FOOD_ORDERING_APP_TITLE", "Food Ordering API")
    description = os.getenv("FOOD_ORDERING_APP_DESCRIPTION", "API for a food ordering system")
    
    api = Api(app, version=app_version, title=app_title, description=description) 
    
    register_routes(api)
    
    # Register routes
    
    
    return app
    
