from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///OneToMany.sqlite3"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    notes = db.relationship("Notes", backref="user")

    def __repr__(self) -> str:
        return f"<User:{self.name}>"  # yaha user obj ka string me representation is happenening in which user_name is there..


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))

    # cascade delete = whenever user is deleted its related notes also deleted from Notes Table...

    def __repr__(self) -> str:
        return f"<Note:{self.note}>"


if (
    __name__ == "__main__"
):  # checks script is directly run or not  or imported from any other script....
    app.run(debug=True)


