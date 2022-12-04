from flask import Blueprint, render_template
from database import db

blood_data = Blueprint('blood_data', __name__, template_folder='templates')


@blood_data.route('/blood_data', methods=['POST', 'GET'])
def blood_data_():
    result = False
    with db.cursor() as cursor:
        query = "SELECT *  FROM blood;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        res = []
        for rw in result:
            row = []
            row.append({rw[0]: True})
            row.append({rw[1]: True})
            row.append({rw[2]: True})
            row.append({rw[3]: True})
            # row.append({rw[4]: True})
            # row.append({rw[5]: True})
            res.append(row)
        result = res
        print("****************************************************************")
        print(result)
        return render_template("blood_data.html", result = result)
    print("****************************************************************")
    print(result)
    return render_template("blood_data.html",result=result)


__all__ = ["blood_data"]