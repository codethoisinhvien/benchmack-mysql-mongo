from pymongo import MongoClient
import time
class mongo_database:
    def __init__(self):
      
 
        self.client =  MongoClient("mongodb://localhost:27017/")
        self.db=self.client["giant_db"]
    def findAll(self):
        start = time.clock()
        for x in self.db["rentals"].find():
            pass
        end = time.clock()
        return end-start
    def findOne(self):
        start = time.clock()
        self.db["rentals"].find ({"id":38238})
        end = time.clock()
       # result = self.cur.fetchall()
   
        return end -start
       
    def updateOne(self):
        start = time.clock()
        res=self.db["rentals"].update_one ({"id":38238},{"$set":{"status;":1}})
        end = time.clock()
        return end-start
    def updateMore(self):
        start = time.clock()
        res=self.db["rentals"].update_many({"id_user":2},{"$set":{"status;": 0}})
        print(res)
        end = time.clock()
        return end-start
    def deleteOne(self):
        start = time.clock()
        res=self.db["rentals"].delete_one({"id":502})
        print(res)
        end = time.clock()
        return end-start
    def deleteMore(self):
        start = time.clock()
        res=self.db["rentals"].delete_many({"id_user": 2})
        print(res)
        end = time.clock()
        return end-start
    def count(self):
        start = time.clock()
        self.db["rentals"].count()
       
        end = time.clock()
        return end-start
    def joinTwo(self):
        start = time.clock()
        res= self.db["rentals"].aggregate([{"$match": {"id": 1002}},{"$lookup": { "from": "users", "localField": "id_user", "foreignField": "id", "as": "rental" }},{ "$unwind": "$rental" }])
        print(res)
        end = time.clock()
        return end-start
        