from flask import Flask, request, render_template, redirect
# from init_db import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zqtdcdqbcofuss:1ULYi0MtfAD3hWxf13rnr7jcTM@ec2-54-204-41-249.compute-1.amazonaws.com:5432/d1mj2esi0svfkn'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=False) #, unique=True
    email = db.Column(db.String(120),unique=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r, Email %r>' % (self.username, self.email)

db.create_all()
# admin = User('hi', 'hi@example.com')
# guest = User('bye', 'bye@example.com')

# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

@app.route("/home")
def index():
	bobaorders = User.query.all()
	return render_template('index.html',bobaorders=bobaorders)

@app.route("/api/boba", methods=["POST"])
def receive_bobaorder():
    print(request.form)
    # db_add_bobaorder(request.form['name'], request.form['bobaorder'])
    neworder = User(request.form['name'], request.form['bobaorder'])
    db.session.add(neworder)
    db.session.commit()
    return redirect("/home")

if __name__ == "__main__":
    app.run(debug=True)
