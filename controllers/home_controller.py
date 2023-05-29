from flask import Blueprint, render_template, request, session, redirect, url_for

# home_controller = Blueprint("home_controller", __name__)


# @home_controller.route("/personalInfo")
# def home():
#     # Fetch users from the database

#     # Render the home template and pass the users as context
#     return render_template("home.html")


# @home_controller.route("/", methods=["GET"])
# def showForm():
#     return render_template("personalInfo.html")


# @home_controller.route("/", methods=["POST"])
# def processForm():
#     first_name = request.form.get("fname")
#     # Store the form data in the session
#     session["first_name"] = first_name
#     return redirect(url_for("home_controller.experience"))


# @home_controller.route("/experience", methods=["GET"])
# def experience():
#     first_name = session.get("first_name")
#     return render_template("experience.html", first_name=first_name)


# @home_controller.route("/mailingList", methods=["GET"])
# def mailingList():
#     return render_template("mailingList.html")


# @home_controller.route("/summary", methods=["GET"])
# def summary():
#     return render_template("summary.html")
