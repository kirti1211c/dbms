from flask import Blueprint, render_template
from database import db

stock_data = Blueprint('stock_data', __name__, template_folder='templates')


@stock_data.route('/stock_data', methods=['POST', 'GET'])
def stock_data_():
    result = False
    with db.cursor() as cursor:
        query = "SELECT *  FROM stock;"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        res = []
        for rw in result:
            row = []
            row.append({rw[0]: True})
            row.append({rw[1]: True})
            row.append({rw[2]: True})
            # row.append({rw[3]: True})
            # row.append({rw[4]: True})
            # row.append({rw[5]: True})
            res.append(row)
        result = res
        print("****************************************************************")
        print(result)
        return render_template("stock_data.html", result = result)
    print("****************************************************************")
    print(result)
    return render_template("stock_data.html",result=result)


__all__ = ["stock_data"]