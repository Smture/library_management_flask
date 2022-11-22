from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from app.config import Config
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import logging
import warnings

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    ma = Marshmallow(app)
    db.init_app(app)

    #initialize logging
    logging.basicConfig(filename='record.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')

    #initialize models.
    from app.models import models

    #instantiating migrations
    migrate = Migrate(app, db, compare_type=True)

    #register blueprints.
    from app.routes import api_routes
    app.register_blueprint(api_routes)

    from app.binders import configure
    FlaskInjector(app=app, modules=[configure])


    return app
