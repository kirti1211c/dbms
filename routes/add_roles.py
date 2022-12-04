from flask import Blueprint, render_template, request, redirect , url_for
from database import db
import sys



add_roles = Blueprint('add_roles', __name__, template_folder='templates')


@add_roles.route('/add_roles', methods=['POST', 'GET'])
def add_roles_():
    id1=0
    person=""
    description=""
    if request.method == "POST":
        id1=request.form.get("id1")
        person=request.form.get("person")
        description=request.form.get("description")
        # with db.cursor() as c:
        #     try:
        #         c.execute("SET FOREIGN_KEY_CHECKS=0;")
        #         print("success fore", file=sys.stderr)
        #     except Exception as e:
        #         print("error",file=sys.stderr)
        #         print(e, file=sys.stderr)
        with db.cursor() as cursor:
            result = True
            try:
                print(id1,person, file=sys.stderr)
                cursor.execute(f'INSERT INTO roles(role_id, role_name, role_desc) VALUES(%s, %s, %s)', (id1, person, description))
                print("success", file=sys.stderr)
            except Exception as e:
                print("excpe",id1,person, file=sys.stderr)
                print(e, file=sys.stderr)
        return redirect(url_for('roles_data.roles_data_'))

    else:
        print("get add_roles", file=sys.stderr)
        return render_template("add_roles.html",id1=id1,person=person,description=description)



__all__ = ["add_roles"]