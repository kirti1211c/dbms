from flask import Flask
from database import db
from routes import test_page

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'some_pass'
app.config['MYSQL_DB'] = 'dbms'
 
db._set_mysql_connection(app=app)

app.register_blueprint(test_page)

app.run(host='0.0.0.0', port=4001)

__all__ = ["app"]