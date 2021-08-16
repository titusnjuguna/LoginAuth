from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, Length , EqualTo


class RegistrationForm(FlaskForm):

    username = StringField('username_label',
               validators=[InputRequired(message="Username is required"),
               Length(min=5, max=30,message="Username must be between 5 and 29 characters")])
    email =  StringField('email_label',
            validators=[InputRequired(message="Email is required"),
            Length(min=20, max=70,message="Email must be between 20 and 69 characters")])
    password = PasswordField('password_label',
                validators=[InputRequired(message="Password is required"),
                Length(min=5, max=30,message="Password must be between 5 and 29 characters")])
    confirm_password = PasswordField('password_field',
                        validators=[InputRequired(message="Password is required"),
                        EqualTo('password',message="password must match")])
    submit_button = SubmitField("Create Account")                    


class Login_form(FlaskForm):
        email =  StringField('email_label',validators=[InputRequired(message="Email is required"),
            Length(min=20, max=70,message="Email must be between 20 and 69 characters")])
        password = PasswordField('password_label', validators=[InputRequired(message="Password is required")]) 
        submit_button = SubmitField("Login")
        Remember_Me = BooleanField()