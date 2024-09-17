from flask import Flask, render_template, redirect, url_for

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


# create a user model

class User(db.Model):
    username = db.Column(db.String(255), unique=True) 
    email = db.Column(db.String(30), primary_key=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    
    

@app.route('/')
def index():
    return render_template('index.html')








if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1',debug=True)