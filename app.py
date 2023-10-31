from flask import Flask, render_template, request, flash, redirect, session
from model import Database
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = '@#$123456&*()'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:''@localhost/property_database'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

db = Database()
alchemy = SQLAlchemy(app)

class User(alchemy.Model):
  __tablename__ = 'user'
  fullname = alchemy.Column(alchemy.String(100))
  email = alchemy.Column(alchemy.String(100))
  username = alchemy.Column(alchemy.String(20), primary_key = True)
  password = alchemy.Column(alchemy.String(50))

  def __init__(self, fullname, email, username, password):
    self.fullname = fullname
    self.email = email
    self.username = username
    self.password = password

  def __repr__(self):
    return '[%s,%s,%s,%s, %s]' % \
    (self.fullname, self.email, self.username, self.password)

@app.route('/')
def index():
  return render_template('index.html', homeActive=True)

@app.route('/about')
def about():
  return render_template('/pages/about-us.html', aboutActive=True)


@app.route('/contact')
def contact():
  return render_template('/pages/contacts.html', contactActive=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if db.checklogin(request.form):
      session['username'] = request.form['username']
      return redirect('/')
    else:
      flash('Username or Password are wrong')
      return redirect('/login')
  return render_template('/pages/login.html', loginActive=True)

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect('/')

@app.route('/register', methods =['GET', 'POST'])
def register():
  if request.method == 'POST':
    if request.form['password'] == request.form['confirm']:
      if db.checkuser(request.form):              
        fullname = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        query = User(fullname,email,username,password)
        alchemy.session.add(query)
        alchemy.session.commit()
        flash('Register successed!')
        return redirect('/login')
      else:
        flash('Username has already taken, please try another!')
        return redirect('/register')
    else:
      flash('Password does not match')
      return redirect('/register')
  return render_template('/pages/register.html', registerActive=True)

@app.route('/insert', methods =['GET', 'POST'])
def insert():
    data = db.option()
    if request.method == 'POST':
        print(request.form)
        if db.insert(request.form):
            flash('Data Berhasil Disimpan')
            return redirect('/table')
        else:
            flash('Data Gagal Disimpan')
            return redirect('/table')
        
    return render_template('/pages/insert.html', insertActive=True, data=data)

@app.route('/property')
def property():
  data = db.read(None)
  print(data)
  return render_template('/pages/property.html', propertyActive=True, data=data)

@app.route('/transaction')
def transaction():
  data = db.readtransaction(None)
  return render_template('/pages/transaction.html', propertyActive=True, data=data)

# admin
@app.route('/manage')
def manage():
  data = db.read(None)
  return render_template('/pages/manage.html',data=data)

@app.route('/delete/<int:id>')
def hapus(id):
    if db.delete(id):
        flash('Data Berhasil Dihapus')
        return redirect('/manage')
    else:
        flash('Data Gagal Dihapus')
        return redirect('/manage')

@app.route('/update/<int:id>')
def edit(id):
  session['id'] = id
  return redirect('/update')

@app.route('/update', methods=['GET','POST'])
def update():
  id = session['id']
  data = db.read(id)
  if request.method == 'POST':
        if db.edit(id, request.form):
            flash('Data Berhasil Diubah')
            session.pop('id', None)
            return redirect('/manage')
        else:
            flash('Data Gagal Diupdate')
            return redirect('/manage')
  return render_template('/pages/update.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)
