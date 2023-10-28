from flask import Flask, render_template, request

app = Flask(__name__)


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