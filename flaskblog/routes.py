from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Album, Author
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated: #Si l'user est déja connecté on le redirige vers la home page
        return redirect(url_for('home'))
    form = RegistrationForm() #On créer le formulaire
    if form.validate_on_submit(): #Si le form est valide:
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #On hash le mdp
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) #On créer un user dans lequel on met les données entrées dans le formulaire
        db.session.add(user) #On ajoute ces données
        db.session.commit() #Et on les insère dans la bd
        flash(f'Votre compte a bien été créer !', 'success') #Un message est affiché si tout à bien fonctionné
        return redirect(url_for('login')) #On redirige vers le form de connnexion
    return render_template('register.html', title='Inscription', form=form)

@app.route("/connexion", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: #Si l'user est déja connecté on le redirige vers la home page
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #Si le mail et le mdp correspondent
            login_user(user, remember=form.remember.data) #on connecte l'user et on le redirige sur la home page
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Connexion échouée, veuillez vérifier votre email et mot de passe', 'danger')
    return render_template('login.html', title='Connexion', form=form)

@app.route("/deconnexion")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/compte", methods=['GET', 'POST'])
@login_required #Permet de ne pas donner l'accès a la page si on n'est pas connecté
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Votre compte à été mis à jour', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Compte', image_file=image_file, form=form)
