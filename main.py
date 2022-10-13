from app.database import db
from config import Config
import app.products.controllers as products
from flask import Flask, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.BASE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

app.register_blueprint(products.module)

db.init_app(app)
with app.test_request_context():
    db.create_all()

if app.debug == True:
    try:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension(app)
    except:
        pass


@app.route("/", methods=["get"])
def start():
    return jsonify({ 'status': 'API working...' })


if __name__ == '__main__':
    app.run(port=5000)


