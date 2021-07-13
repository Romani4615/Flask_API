#import packages/modules
from flask import Flask
#from . import routes

from config import Config
#import routes fvrom blueprints blueprint object from blueprints routes file the variable from init.py file
from .site.routes import site
#define flask app instance of flask object
from .authentication.routes import auth

#import db stuff
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_migrate import Migrate, migrate
from .models import db

app = Flask(__name__)

#register blueprints SITE IS BLUEPRINT OBJECT OF THIS FILE
app.register_blueprint(site)
app.register_blueprint(auth)

#config app based on config class
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

from . import models