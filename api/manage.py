from flask.cli import FlaskGroup

from app import app, db
from app.model.tables import User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(name="giovana", email="giovana@email.com", password="1234", celular="999999999", tipo_de_user=True))
    db.session.commit()

if __name__ == "__main__":
    cli()