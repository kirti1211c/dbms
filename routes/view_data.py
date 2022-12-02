from flask import Blueprint, render_template
from database import db



view_data = Blueprint('view_data', __name__, template_folder='templates')


@view_data.route('/view_data', methods=['POST', 'GET'])
def view_data_():

    return render_template("view_data.html")


__all__ = ["view_data"]