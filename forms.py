from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(message='Ce champs est requis'), Length(min=2, max=20, message='Votre username doit faitre entre 2 et 20 caractères.')])
    email = EmailField('Email',
                            validators=[DataRequired(message='Ce champs est requis'), Email()])
    password = PasswordField('Mot de passe',
                            validators=[DataRequired(message='Ce champs est requis')])
    confirm_password = PasswordField('Confirmer mot de passe',
                            validators=[DataRequired(message='Ce champs est requis'), EqualTo('password', message='Vos mots de passes ne correspondent pas.')])
    submit = SubmitField("S'incrire")

class LoginForm(FlaskForm):
    email = EmailField('Email',
                            validators=[DataRequired(message='Ce champs est requis'), Email()])
    password = PasswordField('Mot de passe',
                            validators=[DataRequired(message='Ce champs est requis')])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField("Se connecter")