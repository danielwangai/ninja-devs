from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# local imports
from config import app_config
from app.views import UserLogin, UserResource
from app.models import db


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


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
    app.register_blueprint(api_blueprint)

    # define endpoints
    api.add_resource(UserResource, "/api/v1/auth/register",
                     endpoint="user_register"
                     )
    api.add_resource(UserLogin, "/api/v1/auth/login",
                     "/api/v1/users",
                     endpoint="user_login"
                     )

    migrate = Migrate(app, db)
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    return app
