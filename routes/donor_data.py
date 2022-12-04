from flask import Blueprint, render_template
from database import db

donor_data = Blueprint('donor_data', __name__, template_folder='templates')


@donor_data.route('/donor_data', methods=['POST', 'GET'])
def donor_data_():
    result = False
    with db.cursor() as cursor:
        query = "SELECT *  FROM donor;"
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
            row.append({rw[4]: True})
            row.append({rw[5]: True})
            res.append(row)
        result = res
        print("****************************************************************")
        print(result)
        return render_template("donor_data.html", result = result)
    print("****************************************************************")
    print(result)
    return render_template("donor_data.html",result=result)


__all__ = ["donor_data"]