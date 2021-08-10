from flask import Flask,render_template,redirect,url_for,request,session
#from models import *
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from wtf_fields import *
import os


app = Flask(__name__)
app.secret_key = os.urandom(16)

#configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tito:208251001@localhost:5432/register"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)
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

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")
    """ 
    user = get_user(request.form['username'])

    if user.check_password(request.form['password']):
        login_user(user)
        app.logger.info('%s logged in successfully', user.username)
        return redirect(url_for('index'))
    else:
        app.logger.info('%s failed to log in', user.username)
        abort(401)
    """

@app.route('/register',methods=['GET','POST'])
def register():
    reg_form = RegistrationForm()
    if request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username =='' or email == '':
            return render_template('auth/register.html',message='please enter required fields')
        if db.session.query(User_model).filter(User_model.username==username).count()==0:
            user = User_model(username,email,password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html',message='username exist!')     
    return render_template("register.html",form = reg_form)

            
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)
