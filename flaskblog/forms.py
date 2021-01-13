from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField
from flaskblog.models import User

#Création du formulaire d'inscription
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

    def validate_username(self, username): #On vérifie que l'utilisateur entré dans le form n'existe pas déja
        user = User.query.filter_by(username=username.data).first()
        if user: #Si il existe, on renvoie un message d'erreur
            raise ValidationError('Cet username existe déja, veuillez en choisir un autre.')
    
    def validate_email(self, email): #Meme chose pour l'email
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cet email existe déja, veuillez en choisir une autre.')

#Création du formulaire de connexion
class LoginForm(FlaskForm):
    email = EmailField('Email',
                            validators=[DataRequired(message='Ce champs est requis'), Email()])
    password = PasswordField('Mot de passe',
                            validators=[DataRequired(message='Ce champs est requis')])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField("Se connecter")

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(message='Ce champs est requis'), Length(min=2, max=20, message='Votre username doit faitre entre 2 et 20 caractères.')])
    email = EmailField('Email',
                            validators=[DataRequired(message='Ce champs est requis'), Email()])
    submit = SubmitField("Mettre à jour")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Cet username existe déja, veuillez en choisir un autre.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Cet email existe déja, veuillez en choisir une autre.')

class AlbumForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired(message='Ce champs est requis')])
    release_year = IntegerField('Année de sortie', validators=[DataRequired(message='Ce champs doit être remplis')])
    author_id = StringField('Nom de l\'auteur', validators=[DataRequired()])
    submit = SubmitField('Ajouter')

class GenreForm(FlaskForm):
    name = StringField('Nom du genre', validators=[DataRequired(message='Ce champs est requis')])
    submit = SubmitField('Ajouter')


class AuthorForm(FlaskForm):
    name = StringField('Nom de l\'auteur', validators=[DataRequired(message='Ce champs est requis')])
    submit = SubmitField('Ajouter')

class AlbumSearchForm(FlaskForm):
    search = StringField('')
    submit = SubmitField('Rechercher')
