from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy



# local imports
from config import app_config

db = SQLAlchemy()


def create_app(config_mode):
    """
    To create application factory.
    This allows creation of app instances.

    :param config_mode: can be development, testing or production
    :return: app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_mode])

    from app import models
    db.init_app(app)

    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    return app
