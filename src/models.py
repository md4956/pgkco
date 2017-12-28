import sqlite3 as sql
from werkzeug.security import check_password_hash
from pymongo import MongoClient


# connect to mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.pgco
collection = db.users


# manage SQLite3 db, insert user
def insertUser(username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username, password))
    con.commit()
    con.close()


# manage SQLite3 db, retrieve user
def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users


# # Define the Role data-model
# class Role:
#     __tablename__ = 'roles'
#     id = collection['_id']
#     email = collection['email']
#
#
# # Define the UserRoles association table
# class UserRoles:
#     __tablename__ = 'user_roles'
#     id = collection['_id']
#     user_id = collection['_id']
#     role_id = collection['role']


# class User():
#
#     def __init__(self, username):
#         self.username = username
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.username
#
#     @staticmethod
#     def validate_login(password_hash, password):
#         return check_password_hash(password_hash, password)

