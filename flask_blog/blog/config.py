import os

class BaseConfig(object):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI='sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='vstavayproklyatyemzakleymlyonnyiy1917'


class DevConfig(BaseConfig):
    DEBUG=True
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

class TestConfig(BaseConfig):
    TESTING=True
