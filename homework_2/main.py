from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = b"4f8cc245e5e09ba315d1060ba656ab43a2e11f75a909c3a77accd3b7a6f308a7"

# генерация надежного секретного ключа
# python
# >>> import secrets
# >>> secrets.token_hex()


@app.route("/", methods=["GET", "POST"])
def base():
    context = {"base": "Авторизация"}
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        return redirect(url_for("autorisation"))
    return render_template("base.html", **context)


@app.route("/autorisation/", methods=["GET", "POST"])
def autorisation():
    if "name" in session:
        context = {
            "name": session["name"],
            "email": session["email"],
            "title": "Добро пожаловать",
        }
        if request.method == "POST":
            session.pop("name", None)
            session.pop("email", None)
            return redirect(url_for("base"))
        return render_template("autorisation.html", **context)
    else:
        return redirect(url_for("base"))


if __name__ == "__main__":
    app.run(debug=True)
