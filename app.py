from flask import Flask, render_template, request, flash, redirect, session
from model import Database
app = Flask(__name__)
app.secret_key = '@#$123456&*()'

db = Database()

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
    temp = db.checklogin(request.form)
    if not temp:
      flash('Username or Password are wrong')
      return redirect('/login')
    session['username'] = temp[0]
    session['role'] = temp[1]
    return redirect('/')
  return render_template('/pages/login.html', loginActive=True)


@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect('/')

@app.route('/register', methods =['GET', 'POST'])
def register():
  if request.method == 'POST':
    if request.form['password'] == request.form['confirm']:
        temp = db.adduser(request.form)                 
        flash(temp[0])
        return redirect(temp[1])
    else:
      flash('Password does not match')
      return redirect('/register')
  return render_template('/pages/register.html', registerActive=True)

@app.route('/insert', methods =['GET', 'POST'])
def insert():
    data = db.option()
    if request.method == 'POST':
        print(request.form)
        flash(db.insert(request.form))
        return redirect('/manage')
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
    flash(db.delete(id))
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
