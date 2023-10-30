import pymysql

class Database:
    def connect(self):
<<<<<<< HEAD
        return pymysql.connect(host='localhost', user='root', password='', database='property_database', charset='utf8mb4')

    def option(self):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM property_category')
=======

        return pymysql.connect(host='localhost', user='root', password='', database='property_database', charset='utf8mb4')
    
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            if id == None:
                cursor.execute('SELECT * FROM properties')
            else:
                cursor.execute('SELECT * FROM properties where id = %s',(id,))
>>>>>>> 9aad09c8846d8899a4086d49fafb620e71436586
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
<<<<<<< HEAD

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
=======
            
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
>>>>>>> 9aad09c8846d8899a4086d49fafb620e71436586
        finally:
            con.close()