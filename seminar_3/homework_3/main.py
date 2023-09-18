import hashlib

from flask import Flask, redirect, request, render_template, session, url_for
from flask_wtf.csrf import CSRFProtect
import binascii
from homework_3.forms import RegistrationForm
from homework_3.models import db, User

app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = b"4f8cc245e5e09ba315d1060ba656ab43a2e11f75a909c3a77accd3b7a6f308a7"
csrf = CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///users.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        birthdate = form.birthdate.data
        password = form.password.data

        dk = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=bytes(password, "utf-8"),
            salt=b"bad_salt",
            iterations=100000,
        )
        password = binascii.hexlify(dk)

        personal_data = form.personal_data.data

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            error_msg = "Пользователь с таким именем или email уже существует."
            form.username.errors.append(error_msg)
            return render_template("register.html", form=form)
        new_user = User(
            username=username,
            email=email,
            birthdate=birthdate,
            password=password,
            personal_data=personal_data,
        )
        db.session.add(new_user)
        db.session.commit()
        session["username"] = request.form.get("username")
        session["email"] = request.form.get("email")
        return redirect(url_for("autorisation"))

    return render_template("register.html", form=form)


@app.route("/autorisation/", methods=["GET", "POST"])
def autorisation():
    if "username" in session:
        context = {
            "username": session["username"],
            "email": session["email"],
            "title": "Добро пожаловать",
        }
        if request.method == "POST":
            session.pop("username", None)
            session.pop("email", None)
            return redirect(url_for("base"))
        return render_template("autorisation.html", **context)
    else:
        return redirect(url_for("base"))
