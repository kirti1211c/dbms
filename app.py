from flask import Flask
from database import db
from routes import test_page, home_page, view_data, roles_data, add_employee, add_roles, employee_data, patient_data, hospital_data, donor_data, blood_data, stock_data, stores_data
# from flask_session import Session

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'some_pass'
app.config['MYSQL_DB'] = 'dbms'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
 
db._set_mysql_connection(app=app)

app.register_blueprint(test_page)
app.register_blueprint(home_page)
app.register_blueprint(view_data)
app.register_blueprint(roles_data)
app.register_blueprint(add_employee)
app.register_blueprint(employee_data)
app.register_blueprint(hospital_data)
app.register_blueprint(blood_data)
app.register_blueprint(donor_data)
app.register_blueprint(patient_data)
app.register_blueprint(stock_data)
app.register_blueprint(stores_data)
app.register_blueprint(add_roles)
app.run(host='0.0.0.0', port=4001)

__all__ = ["app"]