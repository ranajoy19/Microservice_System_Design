import jwt ,os
from flask import Flask,request
from flask_mysqldb import MySQL

from dotenv import load_dotenv

load_dotenv()



server = Flask(__name__)
mysql = MySQL(server)


# DATA BASE CONFIG
server.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
server.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
server.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
server.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
server.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT')



@server.route('/login',method=['POST'])
def login():
    auth = request.authorization

    if not auth:
        return "missing credentials",401

    cur  = mysql.connection.cursor()
    res=cur.execute("select email, password from user where email=%s",(auth.username,))
    if res>