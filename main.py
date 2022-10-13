from crypt import methods
from config import Config
from flask import Flask, jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = Config.BASE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS


@app.route("/", methods=["get"])
def start():
    return jsonify({ 'status': 'API working...' })

if __name__ == '__main__':
    app.run(port=5000)
