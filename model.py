import pymysql

class Database:
    def connect(self):

        return pymysql.connect(host='localhost', user='root', password='', database='property_database', charset='utf8mb4')
    
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