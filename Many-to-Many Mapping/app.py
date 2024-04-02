from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ManyToMany.db"

db = SQLAlchemy(app)

user_page = db.Table(  # its a junction table it contains user_id & page_id which represnts m-t-m relations..
    "user_page",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("page_id", db.Integer, db.ForeignKey("page.id")),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    following = db.relationship("Page", secondary=user_page, backref="followers")

    """ following == represents users & pages ke beech me m-t-m relations.
        backref = followers == used to establish reverse relationship b/w page & user class..
        sqlal automatically called  property i.e. followers on page class which allows to access all users who are in that page."""

    def __repr__(self) -> str:  # represents in  readable manner

        return f"<User:{self.name}>"  #  user obj ko representing in str format...


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self) -> str:
        return (
            f"<page:{self.name}>"
            """username ko str ke format me return kregaa..
                                    if repr ko use nhi krenge to woh default object's memory address print kregaa ..
                                        which is not readble & user-freiendly..."""
        )


if __name__ == "__main__":
    app.run(debug=True)


