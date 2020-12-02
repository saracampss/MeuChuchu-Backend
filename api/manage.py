from flask.cli import FlaskGroup

from app import app, db
from app.model.tables import User 
from sqlalchemy import create_engine

cli = FlaskGroup(app)

engine = create_engine('postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev')

@cli.command("create_db")
def create_db():
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(name="giovana", email="giovana@email.com", password='sara1234', celular="999999999", tipo_de_user=True))
    db.session.commit()
    
# def add_column(engine, table_name, column):
#     column_name = column.compile(dialect=engine.dialect)
#     column_type = column.type.compile(engine.dialect)
#     engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))

# bancas = "bancas"
# users = "users"
# produtos = "produtos"

# column = db.Column('image', db.Text, primary_key=False)
# add_column(engine, produtos, column)
# add_column(engine, bancas, column)
# add_column(engine, users, column)

if __name__ == "__main__":
    cli()