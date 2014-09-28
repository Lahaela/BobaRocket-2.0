import sqlite3
import time
from flask import Flask, request, g
from server1 import app, db, User

# DATABASE = 'bobaorders.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

# def db_read_bobaorders():
#     c = get_db().cursor()
#     c.execute("SELECT * FROM bobaorders")
#     return c.fetchall()

# def db_add_bobaorder(name, bobaorder):
#     c = get_db().cursor()
#     t = str(time.time())
#     boba_info = (name, t, bobaorder)
#     c.execute("INSERT INTO bobaorders VALUES (?, ?, ?)", boba_info)
#     get_db().commit()


db.create_all()
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()