from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "postgresql://postgres:1992@localhost/height_collector"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#  create model objects 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16))
    email = db.Column(db.String(32), unique=True)
    
    def __repr__(self):
        return '<User %r>' % self.username
 
 
# 1. create a table 
db.create_all()
print("Created Successfully!")

usr2 = User(id=2, username="yang", password="yang", email="yang@163.com")
db.session.add(usr2)
print("Add usr2")
db.session.commit()


#The above works great