from flask import Flask, request, render_template, redirect
from init_db import *
# from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username

@app.route("/home")
def index():
	bobaorders = db_read_bobaorders()
	print(bobaorders)
	return render_template('index.html',bobaorders=bobaorders)

@app.route("/api/boba", methods=["POST"])
def receive_bobaorder():
    print(request.form)
    db_add_bobaorder(request.form['name'], request.form['bobaorder'])
    return redirect("/home")

if __name__ == "__main__":
    app.run(debug=True)
