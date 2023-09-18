from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
    authors = db.relationship(
        "Author", secondary="book_author", backref="books", lazy=True
    )

    def __repr__(self):
        return f"{self.title} {self.year} {self.count} {self.authors}"


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    def __repr__(self):
        return f"{self.book_id} {self.author_id}"
