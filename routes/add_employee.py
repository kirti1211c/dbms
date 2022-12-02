from flask import Blueprint, render_template, request, redirect , url_for
from database import db
import sys



add_employee = Blueprint('add_employee', __name__, template_folder='templates')


@add_employee.route('/add_employee', methods=['POST', 'GET'])
def add_employee_():
    id1=0
    person=""
    phone_no=""
    gmail=""
    home=""
    id2=0
    if request.method == "POST":
        id1=request.form.get("id1")
        person=request.form.get("person")
        phone_no=request.form.get("phone_no")
        gmail=request.form.get("gmail")
        home=request.form.get("home")
        id2=request.form.get("id2")
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
                cursor.execute(f'INSERT INTO employee(employee_id, name, mobile_no, email, address,role_id) VALUES(%s, %s, %s, %s, %s, 8459)', (id1, person, phone_no, gmail,home))
                print("success", file=sys.stderr)
            except Exception as e:
                print("excpe",id1,person, file=sys.stderr)
                print(e, file=sys.stderr)
        return redirect(url_for('employee_data.employee_data_'))

    else:
        print("get add_employee", file=sys.stderr)
        return render_template("add_employee.html",id1=id1,id2=id2,person=person,phone_no=phone_no,gmail=gmail,home=home)



__all__ = ["add_employee"]