from flask import Blueprint, render_template
from models import User

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/')
def home():
    # Fetch users from the database
    users = User.get_all()

    # Render the home template and pass the users as context
    return render_template('home.html', users=users)