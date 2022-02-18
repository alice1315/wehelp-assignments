from flask import request, session
import json

from . import api_
from .. import db

@api_.route("/members", methods = ["GET"])
def search_member():
    r_username = request.args.get("username")

    sql = ("SELECT id, name, username FROM member WHERE username=%s")
    sql_data = (r_username, )

    result = db.execute_sql(sql, sql_data)
    result_dict = {"data": result}

    return json.dumps(result_dict)

@api_.route("/member", methods = ["POST"])
def update_name():
    if session:
        r_data = request.get_json()
        r_name = r_data["name"]

        if r_name:
            sql = ("UPDATE member SET name=%s WHERE username=%s")
            sql_data = (r_name, session["username"])

            db.execute_sql(sql, sql_data)
            db.cnx.commit()

            session["name"] = r_name

            result = {"ok": True}
            return json.dumps(result)
            
        else:
            result = {"error": True}
            return json.dumps(result)
            
    else:
        result = {"error": True}
        return json.dumps(result)
