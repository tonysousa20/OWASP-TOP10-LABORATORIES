from flask import Flask, render_template, request, redirect, session
from database import init_db, get_user

app = Flask(__name__)
# Intentionally insecure secret for this security laboratory.
app.secret_key = "dev-secret-key"


@app.route("/")
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "tony" and password == "tony123":
            session["user_id"] = 1
            return redirect("/profile/1")

        if username == "antony" and password == "antony123":
            session["user_id"] = 2
            return redirect("/profile/2")

        return "Invalid credentials", 401

    return render_template("login.html")


@app.route("/profile/<int:user_id>")
def profile(user_id):

    if "user_id" not in session:
        return "Unauthorized", 401

    if session["user_id"] != user_id:
        return "Forbidden", 403

    user = get_user(user_id)

    if not user:
        return "User not found", 404

    return render_template("profile.html", user=user)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
