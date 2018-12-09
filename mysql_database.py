import pymysql
import time
class mysql_database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "13081999"
        db = "giant_db"
 
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def findAll(self):
        start = time.clock()
        self.cur.execute("SELECT *FROM rentals")
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def findOne(self):
        start = time.clock()
        self.cur.execute("SELECT *FROM users where id =8920")
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def updateOne(self):
        start = time.clock()
        res = self.cur.execute(" UPDATE rentals SET status =1 where id =90887")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def updateMore(self):
        print("start")
        start = time.clock()
        res = self.cur.execute(" UPDATE rentals SET status =0 where id_user =2")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def deleteOne(self):
        print("start")
        start = time.clock()
        res = self.cur.execute(" DELETE from  rentals where id =9089")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def deleteMore(self):
        print("start")
        start = time.clock()
        res = self.cur.execute(" DELETE from  rentals where id <100")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def count(self):
        print("start")
        start = time.clock()
        res = self.cur.execute(" Select count(*) from  rentals ")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start
    def joinTwo(self):
        print("start")
        start = time.clock()
        res = self.cur.execute(" Select *form rentals join user on rentals.id_user=users.id")
        print(res)
        end = time.clock()
       # result = self.cur.fetchall()
 
        return end -start