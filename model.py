import pymysql

class Database:
    def connect(self):
        return pymysql.connect(host='localhost', user='root', password='', database='property_database', charset='utf8mb4')

    def option(self):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM property_category')
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close() 
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM properties')
            else:
                cursor.execute('SELECT * FROM properties where id = %s',(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO properties(name, address, category_id, price, description) VALUES(%s, %s, %s, %s, %s)',
                                (data['name'], data['address'], data['category_id'], data['price'], data['description'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
            
    def readtransaction(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM transactions')
            else:
                cursor.execute('SELECT * FROM transactions where id = %s',(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def checkuser(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user where username = %s',(str(data['username']),))
            if len(cursor.fetchall()) == 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()

    def adduser(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('INSERT INTO user(fullname, email, username, password) VALUES(%s, %s, %s, %s)',
                                (data['fullname'], data['email'], data['username'], data['password'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def checklogin(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM user where username = %s and password = %s',(data['username'],data['password'],))
            if len(cursor.fetchall()) != 0:
                return True
            else:
                return False
        except:
            return False
        finally:
            con.close()