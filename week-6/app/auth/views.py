from flask import request, session, redirect, render_template, url_for

from ..models import database
from app.config import MYSQL_CONFIG

from . import auth

@auth.before_request
def before_request():
    global cnx ,cursor
    (cnx, cursor) = database.get_cursor(MYSQL_CONFIG)

@auth.route("/signup", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":

        r_name = request.form["name"]
        r_username = request.form["username"]
        r_password = request.form["password"]

        find_user = ("SELECT * FROM member WHERE username = %s")

        cursor.execute(find_user, (r_username, ))
        count = cursor.fetchone()

        if (not r_name or not r_username or not r_password):
            return redirect(url_for("auth.show_error", message = "請輸入註冊資料"))

        elif count:
            return redirect(url_for("auth.show_error", message = "帳號已經被註冊"))

        else:
            add_user = ("INSERT INTO member"
                        "(name, username, password)"
                        "VALUES (%s, %s, %s)")

            user_data = (r_name, r_username, r_password)

            cursor.execute(add_user, user_data)
            cnx.commit()
            return redirect("/")

    else:
        return redirect("/")

@auth.route("/signin", methods = ["GET", "POST"])
def sign_in():
    if request.method == "POST":

        r_username = request.form["username"]
        r_password = request.form["password"]

        find_user = ("SELECT * FROM member WHERE username = %s LIMIT 1")

        cursor.execute(find_user, (r_username, ))
        user = cursor.fetchone()

        if (not r_username or not r_password):
            return redirect(url_for("auth.show_error", message = "請輸入帳號、密碼"))

        elif user == None:
            return redirect(url_for("auth.show_error", message = "查無此帳號"))
        
        else:
            if r_password == user["password"]:
                session["name"] = user["name"]
                return redirect("/member")
            else:
                return redirect(url_for("auth.show_error", message = "密碼輸入錯誤"))

    else:
        return redirect("/")

@auth.route("/signout", methods = ["GET"])
def sign_out():
    session.clear()
    return redirect("/")

@auth.route("/error/", methods = ["GET"])
def show_error():
    message = request.args.get("message")
    return render_template("error.html", message = message)

@auth.after_request
def after_request(resp):
    global cnx, cursor
    if cnx:
        cursor.close()
        cnx.close()
    return resp
