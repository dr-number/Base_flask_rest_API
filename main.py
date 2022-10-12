from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "<p>Hello, flask!</p>"

if __name__ == '__main__':
    #app.run(host="0.0.0.0")
    app.run(port=5000)