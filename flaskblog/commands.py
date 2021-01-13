from flaskblog import app, db
from flaskblog.models import Author, Album
import click
import json



@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    db.create_all()
    albums = json.load(open(filename))

    authors = {}
    for album in albums:
        a = album["parent"]
        if a not in authors:
            o = Author(name = a)
            db.session.add(o)
            authors[a] = o
    db.session.commit()

    for album in albums:
        a = authors[album["parent"]]
        o = Album(
            title = album["title"],
            release_year = album["realeaseYear"],
            img = album["img"],
            author_id = a.id
        )
        db.session.add(o)
    db.session.commit()

@app.cli.command()
def syncdb():
    db.create_all()