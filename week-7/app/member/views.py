from flask import session, redirect, render_template

from . import member

@member.route("/member", methods = ["GET"])
def show_member():
    if not session:
        return redirect("/")
    else:
        return render_template("member.html", name = session["name"])
