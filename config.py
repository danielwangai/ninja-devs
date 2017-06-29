import os

class Config(object):
    """
    Common configurations.
    """
    DEBUG = False


class Development(Config):
    """
    Development configurations.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@localhost/{}'.format(
        os.getenv('DB_NINJAS_USERNAME'), os.getenv('DB_PASSWORD'),
        os.getenv('NINJAS_DB_NAME')
    )


class Testing(Config):
    """
    Testing configurations.
    """
    # Debug is set to false
    base_dir = os.path.join(os.path.dirname(__file__))
    # define test db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(
        base_dir, 'ninjas_test.db'
    )


class Production(Config):
    """
    Production configurations.

    DEBUG = False because this class inherits from Config class.
    """


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
