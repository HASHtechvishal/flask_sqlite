from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(120), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'Item {self.name}'



@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
