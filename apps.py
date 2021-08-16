from flask import Flask,render_template,redirect,url_for,request,session,abort,flash
from models import *
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from wtf_fields import *
from flask_login import UserMixin, login_user,LoginManager,login_required,logout_user,current_user
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(16)

#configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tito:208251001@localhost:5432/register"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app,db)

login_manager =LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User_model.query.get(int(id))


class User_model(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String(),nullable=False)

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    def __repr__(self):
        return f'<User {self.username}>'
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)


def redirect_dest(fallback):
    dest = request.args.get('next')
    try:
        dest_url = url_for(dest)
    except:
        return redirect(fallback)
    return redirect(dest_url)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/home')
@login_required
def base():
    return render_template("base.html")


@app.route('/login', methods=['GET','POST'])
def login():
    form = Login_form()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        user =User_model.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            login_user(user)
            flash("login successful")
            #next = request.args.get('next')
            #if not is_safe_url(next):
               # return abort(400)
            return redirect_dest(fallback=url_for('home'))
        else:
             flash('Wrong password or The User doesnt Exist ') 
    else:
        print(form.errors)
    return render_template('login.html', form=form)
                 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))    

@app.route('/register',methods=['GET','POST'])
def register():
    reg_form = RegistrationForm()
    if request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username =='' or email == '':
            return render_template('register.html',message='please enter required fields')
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
