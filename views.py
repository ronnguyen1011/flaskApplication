from flask import render_template, redirect, url_for, session, request
from models import UserInfo

def show_form():
    return render_template("personalInfo.html")

def process_form():
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")
    state = request.form.get("state")
    phone = request.form.get("phone")
    ml_signup = bool(request.form.get("MLSignUp"))

    session["first_name"] = first_name
    session["last_name"] = last_name
    session["email"] = email
    session["state"] = state
    session["phone"] = phone
    session["ml_signup"] = ml_signup
    return redirect(url_for("experience_route"))

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

    session["jobs"] = jobs
    session["Industry"] = industry
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

    return render_template("summary.html", user_info=user_info)
