from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "Bestplayers"

    id = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(128), unique=True, nullable=False)
    Position = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, Player, Position):
        self.Player = Player
        self.Position = Position
    def __repr__(self):
        return f"<User {self.Player}>"

@app.route("/")
def hello_world():
        users = User.query.all()
        results = [
            {
                "id": user.id,
                "Player": user.Player,
                "Position": user.Position
            } for user in users]

        return render_template("index.html",results=results)
  
