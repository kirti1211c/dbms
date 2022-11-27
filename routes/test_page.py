import json
from flask import Blueprint, render_template
from database import db

test_page = Blueprint('test_page', __name__, template_folder='templates')

@test_page.route('/test-mysql-dump', methods=['GET'])
def test_mysql_dump():
    with db.cursor() as cursor, open("sql/fetch_all_postal_codes_info.sql", "r") as sql:
        cursor.execute(sql.read())
        data = cursor.fetchall()

    return render_template("test.html", data=data)

__all__ = ["test_page"]