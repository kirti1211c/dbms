from flask import Blueprint, render_template

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/', methods=['GET'])
def home_page_():

    return render_template("home_page.html")


__all__ = ["home_page"]