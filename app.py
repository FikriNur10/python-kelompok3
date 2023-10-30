from flask import Flask, render_template, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from model import Database
app = Flask(__name__)
app.secret_key = '@#$123456&*()'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:''@localhost/flask2023'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

db = Database()
alchemy = SQLAlchemy(app)



@app.route('/')
def index():
  return render_template('index.html', homeActive=True)

@app.route('/about')
def about():
  return render_template('/pages/about-us.html', aboutActive=True)

@app.route('/table')
def table():
  return render_template('/pages/table.html', tableActive=True)

@app.route('/contact')
def contact():
  return render_template('/pages/contacts.html', contactActive=True)

@app.route('/login')
def login():
  return render_template('/pages/login.html', loginActive=True)

@app.route('/register')
def register():
  return render_template('/pages/register.html', registerActive=True)

@app.route('/property')
def property():
  data = db.read(None)
  return render_template('/pages/property.html', propertyActive=True, data=data)

@app.route('/transaction')
def transaction():
  data = db.readtransaction(None)
  return render_template('/pages/transaction.html', propertyActive=True, data=data)

if __name__ == '__main__':
    app.run(debug = True)