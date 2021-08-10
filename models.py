#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "Wira_db://tito:208251001@localhost:5432/register"
db = SQLAlchemy()
#migrate = Migrate(app,db)
class User_model(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String(),nullable=False)

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = password

#if __name__ =="__main__":
#    app.run()
        