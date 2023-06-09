import re
from flask import render_template, redirect, url_for, session, request
from models import UserInfo
import mysql.connector

# Web Host Database Connection
connection = mysql.connector.connect(
    host="localhost",
    database="nguyenro_db",
    user="nguyenro_test",
    password="Wqk+dGSnFr$v",
)

# Local Host Database Connection
# connection = mysql.connector.connect(
#     host="localhost",
#     database="mydata",
#     user="root",
#     password="",
# )
cursor = connection.cursor()

def show_form(errors=None):
    return render_template("personalInfo.html", errors=errors)


def process_form():
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")
    state = request.form.get("state")
    phone = request.form.get("phone")
    ml_signup = bool(request.form.get("MLSignUp"))

    # Validation start
    errors = []
    if not first_name:
        errors.append("Please enter your first name")
    elif not re.match(r"^[a-zA-Z]+$", first_name):
        errors.append("First name should only contain letters")

    # Validate last_name
    if not last_name:
        errors.append("Please enter your last name")
    elif not re.match(r"^[a-zA-Z]+$", last_name):
        errors.append("Last name should only contain letters")
    # Add more validation checks here if needed

    if errors:
        return show_form(errors=errors)  # Display errors on the form page
    else:
        # Process the form data and store it in session
        session["first_name"] = first_name
        session["last_name"] = last_name
        session["email"] = email
        session["state"] = state
        session["phone"] = phone
        session["ml_signup"] = ml_signup

        return redirect(url_for("experience_route"))
    # Validation end


def experience():
    return render_template("experience.html")


def save_data():
    biography = request.form.get("biography")
    gitLink = request.form.get("gitLink")
    year = request.form.get("fav_language")
    experience = request.form.get("fav_language1")

    session["biography"] = biography
    session["gitLink"] = gitLink
    session["fav_language"] = year
    session["fav_language1"] = experience
    return redirect(url_for("mailing_list_route"))


def mailing_list():
    return render_template("mailingList.html")


def mailing_list_data():
    jobs = request.form.getlist("Jobs")
    industry = request.form.getlist("Industry")

    # Convert lists to strings
    jobs_str = ", ".join(jobs)
    industry_str = ", ".join(industry)

    session["jobs"] = jobs_str
    session["Industry"] = industry_str
    return redirect(url_for("summary_route"))


def summary():
    user_info = UserInfo(
        first_name=session.get("first_name"),
        last_name=session["last_name"],
        email=session["email"],
        state=session["state"],
        phone=session["phone"],
        ml_signup=session["ml_signup"],
        biography=session["biography"],
        git_link=session["gitLink"],
        year=session["fav_language"],
        experience=session["fav_language1"],
        jobs=session["jobs"],
        industry=session["Industry"]
    )
    mailing_list = user_info.jobs + ", " + user_info.industry + "."
    # Save user_info to the database
    insert_query = """
        INSERT INTO applicant (first_name, last_name, email, state, phone, ml_signup, biography, git_link, year, experience, mailing_list)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        session.get("first_name"),
        session["last_name"],
        session["email"],
        session["state"],
        session["phone"],
        session["ml_signup"],
        session["biography"],
        session["gitLink"],
        session["fav_language"],
        session["fav_language1"],
        mailing_list,
    )

    cursor.execute(insert_query, values)
    connection.commit()

    return render_template("summary.html", user_info=user_info)


def admin_page():
    select_query = "SELECT * FROM applicant"
    cursor.execute(select_query)
    applicants = cursor.fetchall()

    return render_template("admin.html", applicants=applicants)

# MySQL table - PHPMyAdmin page
# CREATE TABLE applicant (
#     id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     email VARCHAR(255),
#     state VARCHAR(255),
#     phone VARCHAR(255),
#     ml_signup BOOLEAN,
#     biography TEXT,
#     git_link VARCHAR(255),
#     year VARCHAR(255),
#     experience VARCHAR(255),
#     mailing_list TEXT
# );