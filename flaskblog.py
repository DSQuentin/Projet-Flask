from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b306650e4ca93bc44c0c3f814f191d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



posts = [
    {
        'author' : 'Corvey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted' : 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='A propos')

@app.route("/inscription", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Compte de {form.username.data} créer !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Inscription', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Connexion réussi !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Connexion échouée, veuillez vérifier votre email et mot de passe', 'danger')
    return render_template('login.html', title='Connexion', form=form)




if __name__ == '__main__':
    app.run(debug=True)
