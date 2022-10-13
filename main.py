from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'

@app.route("/")
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)

    db.create_all()    
