from flask import request, session, redirect, render_template, url_for

from . import auth
from .. import db

@auth.route("/signup", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":

        r_name = request.form["name"]
        r_username = request.form["username"]
        r_password = request.form["password"]

        sql = ("SELECT * FROM member WHERE username=%s")
        sql_data = (r_username, )

        result = db.execute_sql(sql, sql_data)

        if (not r_name or not r_username or not r_password):
            return redirect(url_for("auth.show_error", message = "請輸入註冊資料"))

        elif result:
            return redirect(url_for("auth.show_error", message = "帳號已經被註冊"))

        else:
            sql = ("INSERT INTO member"
                        "(name, username, password)"
                        "VALUES (%s, %s, %s)")
            sql_data = (r_name, r_username, r_password)

            db.execute_sql(sql, sql_data)
            db.cnx.commit()

            return redirect("/")

    else:
        return redirect("/")

@auth.route("/signin", methods = ["GET", "POST"])
def sign_in():
    if request.method == "POST":

        r_username = request.form["username"]
        r_password = request.form["password"]

        sql = ("SELECT * FROM member WHERE username=%s LIMIT 1")
        sql_data = (r_username, )

        result = db.execute_sql(sql, sql_data)

        if (not r_username or not r_password):
            return redirect(url_for("auth.show_error", message = "請輸入帳號、密碼"))

        elif result == None:
            return redirect(url_for("auth.show_error", message = "查無此帳號"))
        
        else:
            if r_password == result["password"]:
                session["name"] = result["name"]
                session["username"] = result["username"]
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
