from flask import Flask, render_template, request, flash, redirect, session, make_response
from model import Database
import os
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import pdfkit

app = Flask(__name__)
app.secret_key = '@#$123456&*()'
folder_upload = app.config['UPLOAD_FOLDER'] = os.path.realpath('.')+'\\static\\uploads\\'
app.config['MAX_CONTENT_LENGTH'] = 5 *1024*1024 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

db = Database()

@app.route('/')
def index():
  data = db.read(None)
  return render_template('index.html', homeActive=True, data=data)

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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    data = db.option()
    if request.method == 'POST':
        files = request.files.getlist('files')
        property_data = {
            'name': request.form['name'],
            'address': request.form['address'],
            'category_id': request.form['category_id'],
            'price': request.form['price'],
            'description': request.form['description']
        }
        
        try:
            result = db.insert(property_data)
            if isinstance(result, list):
                inserted_id = result[1]
                # Insert data gambar untuk setiap file yang diunggah
                for file in files:
                    # filename = secure_filename(file.filename)
                    # directory = folder_upload+filename
                    # file.save(directory)
                    # db.insertImage(inserted_id, filename)
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        directory = folder_upload + filename
                        file.save(directory)
                        db.insertImage(inserted_id, filename)
                    else:
                        flash('File ekstensi tidak diizinkan. Harap unggah file dengan ekstensi .jpg, .jpeg, atau .png.')
                        return redirect('/insert')

                flash('Data Berhasil Disimpan')
                return redirect('/manage')
            flash(result)
            return redirect('/insert')
        except:
            flash('Data Tidak Bisa Diupload')
            return redirect('/insert')

    return render_template('/pages/insert.html', insertActive=True, data=data)


@app.route('/property')
def property():
  data = db.read(None)
  return render_template('/pages/property.html', propertyActive=True, data=data)


@app.route('/transaction')
def transaction():
    if session['role'] == 'user':
        data = db.readtransaction(session['username'])
    else:
        data = db.readtransaction(None)
    return render_template('/pages/transaction.html', data=data)


# admin
@app.route('/manage')
def manage():
  data = db.read(None)
  return render_template('/pages/manage.html',data=data)

@app.route('/manageuser')
def manageuser():
  data = db.readusers(None)
  return render_template('/pages/Datauser.html',data=data)

@app.route('/deleteuser/<int:id>')
def delete_user(id):
    
    success = db.delete_user_by_id(id)
    
    if success:
        return redirect('/manageuser')
    else:
        return "Failed to delete user"

@app.route('/edituser/<int:id>')
def edituser(id):
    session['id'] = id
    return redirect('/updateuser')

@app.route('/updateuser', methods=['GET', 'POST'])
def updateuser():
    id = session.get('id')
    data = db.read_user_by_id(id)

    if request.method == 'POST':
        if db.update_user_by_id(id, request.form):
            flash('Data Berhasil Diubah')
            session.pop('id', None)
            return redirect('/manageuser')
        else:
            flash('Data Gagal Diupdate')
            return redirect('/manageuser')

    return render_template('/pages/updateuser.html', data=data[0] if data else None)

@app.route('/delete/<int:id>')
def hapus(id):
    if db.delete(id):
        listImage = db.getAllImage(id)
        if isinstance(listImage, list):
            for image in listImage:
               directory = folder_upload+image
               os.remove(directory)
        db.deleteAllImage(id)
        flash('Data Berhasil Dihapus')
    else:
        flash('Data Gagal Dihapus')
       
    return redirect('/manage')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        username = session['username']
        property = db.read(request.form['propertyId'])
        image_name = db.getAllImage(request.form['propertyId'])
        meet_date=request.form['meetingDate']
        flash(db.addTransaction(image_name[0], meet_date, username, property))
    return redirect('/property')

@app.route('/update/<int:id>')
def edit(id):
  session['id'] = id
  return redirect('/update')

@app.route('/update', methods=['GET','POST'])
def update():
  id = session['id']
  data = db.read(id)
  option = db.option()
  if request.method == 'POST':
        files = request.files.getlist('files')
        property_data = {
            'name': request.form['name'],
            'address': request.form['address'],
            'category_id': request.form['category_id'],
            'price': request.form['price'],
            'description': request.form['description']
        }
        if db.edit(id, property_data):
            listImage = db.getAllImage(id)
            if isinstance(listImage, list):
                for image in listImage:
                   directory = folder_upload+image
                   os.remove(directory)
            db.deleteAllImage(id)

            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    directory = folder_upload + filename
                    file.save(directory)
                    db.insertImage(id, filename)
                else:
                    flash('File ekstensi tidak diizinkan. Harap unggah file dengan ekstensi .jpg, .jpeg, atau .png.')
                    return redirect('/update')
                
            flash('Data Berhasil Diubah')
            session.pop('id', None)
            return redirect('/manage')
        else:
            flash('Data Gagal Diupdate')
            return redirect('/manage')
  return render_template('/pages/update.html', data=data, option=option)

@app.route('/email', methods=['GET', 'POST'])
def email():
    alluser = db.readaccount(None)
    emailuser = db.readaccount(session['username'])
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        to = request.form['emailkepada']
        subject = request.form['subject']
        message = request.form['isiemail']
        app.config['MAIL_USERNAME'] = email
        app.config['MAIL_PASSWORD'] = password
        if to == 'all':
            allemail=[]
            for i in alluser:
                allemail.append(i[2])
            pesan = Message(subject, sender=email, recipients=allemail)
            pesan.body = message
        else:
            pesan = Message(subject, sender=email, recipients=[to])
            pesan.body = message
        try:
            mail = Mail(app)
            mail.connect()
            mail.send(pesan)
            flash('Email Sent to '+ to)
            return redirect('/email')
        except:
            flash('Failed to Sent Email!!')
            return redirect('/email')

    return render_template('pages/email.html', emailactive = True, alluser=alluser, emailuser=emailuser)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        try:
            start_date = request.form['startdate']
            end_date = request.form['enddate']
            category = request.form['category_id']
            data_from_db = db.readdate(start_date, end_date, session['role'], session['username'], category)
            if not data_from_db:
                flash('Cannot generate PDF for empty list.')
                return redirect('/report')
            rendered = render_template('/pages/pdftemplate.html', data_from_db=data_from_db)
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            pdf = pdfkit.from_string(rendered, configuration=config)
            response = make_response(pdf)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'
            return response
        except Exception as e:
            flash('Generate Report Failed')
            return redirect('/report')

    return render_template('/pages/pdf.html')

@app.route('/acctransaksi/<int:id>')
def acctransaksi(id):
    data = db.readtransaction(id)
    if data:
        current_status = data[0][10]

        if current_status == 'PENDING':
            new_status = 'ON MEET'
        elif current_status == 'ON MEET':
            new_status = 'INQUIRY'
        elif current_status == 'INQUIRY':
            new_status = 'IN PAYMENT'
        elif current_status == 'IN PAYMENT':
            new_status = 'COMPLETED'
        else:
            return redirect('/transaction')

        if db.update_status_transaction(id, new_status):
            flash(f'Status transaksi {id} berhasil diubah menjadi {new_status}')
        else:
            flash(f'Gagal mengubah status transaksi {id}')
    else:
        flash(f'Transaksi dengan ID {id} tidak ditemukan')

    return redirect('/transaction')
  
@app.route('/rejecttransaksi/<int:id>')
def rejecttransaksi(id):
	flash(db.rejectStatus(id))
	return redirect('/transaction')
  
if __name__ == '__main__':
    app.run(debug = True)
