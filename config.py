import os

class Config(object):
    __BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    __BASE_NAME = 'db.sqlite'

    BASE_PATH = f'sqlite:///{os.path.join(__BASE_DIR, __BASE_NAME)}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

