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


class Testing(Config):
    """
    Testing configurations.
    """
    # Debug is set to false


class Production(Config):
    """
    Production configurations.

    DEBUG = False because this class inherits from Config class.
    """
