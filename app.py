from flask import Flask , render_template 
from flask_json import FlaskJSON, JsonError, json_response, as_json
from mysql_database import mysql_database
from mongo_database import mongo_database
import time
app = Flask(__name__)
FlaskJSON(app)


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/mysql/1')
def get_mysqlfindOne():
    db = mysql_database()
    def db_query():
        return  db.findOne()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/2')
def get_mysqlfindAll():
    db = mysql_database()
    def db_query():
        return  db.findAll()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/3')
def get_mysqlupdateOne():
    db = mysql_database()
    def db_query():
        return  db.updateOne()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/4')
def get_mysqlupdateMore():
    db = mysql_database()
    def db_query():
        return  db.updateMore()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/5')
def get_mysqldeleteOne():
    db = mysql_database()
    def db_query():
        return  db.deleteOne()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/6')
def get_mysqldeleteMore():
    db = mysql_database()
    def db_query():
        return  db.deleteMore()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/7')
def get_mysqlcount():
    db = mysql_database()
    def db_query():
        return  db.count()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mysql/8')
def get_mysqljoinTwo():
    db = mysql_database()
    def db_query():
        return  db.joinTwo()
       
 
    res = db_query()
    return json_response(result=res)



@app.route('/mongo/1')
def get_mongoFinOne():
    db = mongo_database()
    def db_query():
        return  db.findOne()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/2')
def get_MongoFindAll():
    db = mongo_database()
    def db_query():
        return  db.findAll()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/3')
def get_MongoUpadeOne():
    db = mongo_database()
    def db_query():
        return  db.updateOne()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/4')
def get_MongoUpdateMore():
    db = mongo_database()
    def db_query():
        return  db.updateMore()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/5')
def get_MongoDeleteOne():
    db = mongo_database()
    def db_query():
        return  db.deleteOne()
       
 
    res = db_query()
    return json_response(result=res)

@app.route('/mongo/6')
def get_MongoDeleteMore():
    db = mongo_database()
    def db_query():
        return  db.deleteMore()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/7')
def get_MongoCount():
    db = mongo_database()
    def db_query():
        return  db.count()
       
 
    res = db_query()
    return json_response(result=res)
@app.route('/mongo/8')
def get_MongojoinTwwo():
    db = mongo_database()
    def db_query():
        return  db.joinTwo()
       
 
    res = db_query()
    return json_response(result=res)


if __name__ == '__main__':
    app.run(debug=True)