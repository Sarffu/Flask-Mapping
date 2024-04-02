from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///OneToOne.db"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    profile = db.relationship(
        "Profile", backref="user", uselist=False
    )  # its a'profile' naam ka ek relationship banao 'Profile' class ke saath jiska reference 'user' hoga aur yeh ek hi element hoga (uselist=False).

    def __repr__(self):
        return f"<User:{self.name}>"


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), unique=True
    )

    #    unique = True means for each profile user_id must be there..

    def __repr__(self) -> str:
        return f"<Profile:{self.username}>"


# uselist = False  means relationship b/w user-profile should one to one.. for each user only one profile..

if __name__ == "__main__":
    app.run(debug=True, port=8000)

