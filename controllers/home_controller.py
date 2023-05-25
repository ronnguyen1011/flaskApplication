from flask import Blueprint, render_template

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/')
def home():
    # Fetch users from the database

    # Render the home template and pass the users as context
    return render_template('home.html')

@home_controller.route('/personalInfo')
def personalInfo():
    return render_template('personalInfo.html')

@home_controller.route('/mailingList')
def mailingList():
    return render_template('mailingList.html')