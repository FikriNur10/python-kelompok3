from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('/pages/about-us.html')

@app.route('/contact')
def contact():
  return render_template('/pages/contacts.html')
