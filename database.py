from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def get_marshmallow(app):
    return Marshmallow(app)

def get_sql_alchemy(app):
    return SQLAlchemy(app)
