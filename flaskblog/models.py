from flaskblog import db, login_manager
from flask_login import UserMixin
import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Author(db.Model):

    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    albums = db.relationship('Album', backref='author', lazy=True) #Un author peut avoir plusieurs albums
    
    def __repr__(self):
        return f"Author('{self.name}')"


#albums_genres = db.Table('albums_genres',
#    db.Column('album_id', db.Integer, db.ForeignKey('album.id')),
#    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')))

class Genre(db.Model):

    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Genre('{self.name}')"

class Album(db.Model):

    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    release_year = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(100), nullable=False, default='default_cover.jpg')
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False) #Un album possède un unique author
    #genres = db.relationship('Genre', secondary=albums_genres, backref=db.backref('albums', lazy=True))

    def __repr__(self):
        return f"Album('{self.title}', '{self.date_posted}, '{self.release_year}','{self.img})"

