from flask.cli import FlaskGroup

from project import app, db, User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    Ronaldo = User( "Ronaldo", "Striker" )
    Zidane = User( "Zidane", "Midfielder" )
    Cantona = User( "Cantona", "Midfielder" )
    Crespo = User( "Crespo", "Striker" )
    db.session.add(Ronaldo)
    db.session.add(Zidane)
    db.session.add(Cantona)
    db.session.add(Crespo)
    db.session.commit()


if __name__ == "__main__":
    cli()

