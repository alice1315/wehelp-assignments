from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

app = Flask(__name__, static_folder = "static", static_url_path = "/")
app.secret_key = "asdasdasd"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def sign_in():
    userid = request.form["userid"]
    userpwd = request.form["userpwd"]

    if (userid == "test" and userpwd == "test"):
        session["status"] = "已登入"
        return redirect("/member/")
    elif (not userid or not userpwd):
        return redirect(url_for("error", message = "請輸入帳號、密碼"))
    else:
        return redirect(url_for("error", message = "帳號或密碼輸入錯誤"))

@app.route("/signout")
def signout():
    session["status"] = "未登入"
    return redirect("/")

@app.route("/member/")
def member():
    if session["status"] == "已登入":
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error/")
def error():
    message = request.args.get("message")
    return render_template("error.html", message = message)

app.run(port="3000")
