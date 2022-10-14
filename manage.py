from config import Config
from flask_migrate import Migrate
from app.database import db
from main import app

migrate = Migrate(app, db, render_as_batch=Config.IS_SQL_LITE)
