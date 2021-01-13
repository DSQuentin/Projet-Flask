import click
import yaml


@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    db.create_all()
    albums = yaml.load(open (filename))

    authors = {}
    for album in albums:
        a = album["parent"]
        if a not in authors:
            o = Author(name = a)
            db.session.add(o)
            authors[a] = o
    db.session.commit()

    for album in albums:
        a = album[b["parent"]]
        o = Album(
            title = b["title"],
            release_year = b["realeaseYear"],
            img = b["img"],
            author_id = a.id
        )
        db.session.add(o)
    db.session.commit()

@app.cli.command()
def syncdb():
    db.create_all()