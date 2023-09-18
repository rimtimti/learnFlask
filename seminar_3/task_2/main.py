import random
from flask import Flask, render_template
from task_2.models import db, Author, Book, BookAuthor

app = Flask(__name__)
app.secret_key = b"4f8cc245e5e09ba315d1060ba656ab43a2e11f75a909c3a77accd3b7a6f308a7"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///books.db"
db.init_app(app)


@app.route("/")
def index():
    return "hello"


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("test-data")
def add_test_data():
    COUNT = 10
    for i in range(1, COUNT + 1):
        book = Book(
            title=f"title{i}",
            year=random.randint(1950, 2023),
            count=random.randint(100, 500),
        )
        db.session.add(book)
    for i in range(1, COUNT + 6):
        author = Author(
            firstname=f"name{i}",
            lastname=f"surname{i}",
        )
        db.session.add(author)
    for i in range(1, COUNT + 6):
        book_author = BookAuthor(
            book_id=random.randint(1, COUNT),
            author_id=random.randint(1, COUNT),
        )
        db.session.add(book_author)
    db.session.commit()
    print("books.db заполнена тестовыми данными")


@app.route("/books/")
def get_books():
    books = Book.query.all()
    context = {"books": books}
    return render_template("books.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
