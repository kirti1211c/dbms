from flask import Blueprint, render_template
from database import db

roles_data = Blueprint('roles_data', __name__, template_folder='templates')


@roles_data.route('/roles_data', methods=['POST', 'GET'])
def roles_data_():
    result = False
    with db.cursor() as cursor:
        query = "SELECT *  FROM roles;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        res = []
        for rw in result:
            row = []
            row.append({rw[0]: True})
            row.append({rw[1]: True})
            row.append({rw[2]: True})
            res.append(row)
        result = res
        print("****************************************************************")
        print(result)
        return render_template("roles_data.html", result = result)
    print("****************************************************************")
    print(result)
    return render_template("roles_data.html",result=result)


__all__ = ["roles_data"]