from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    username = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.String(50))

    def __init__(self, fullname, email, username, password):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '[%s,%s,%s, %s]' % \
            (self.fullname, self.email, self.username, self.password)