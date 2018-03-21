from bottle import route, run
from pymongo import MongoClient

# connect to database
connection = MongoClient('localhost')
db = connection.test

# handle to name collection

names = db.names


@route('/')
def hello():
    return {"hello": "lol"}


run(host='localhost', port=8000, debug=True)
