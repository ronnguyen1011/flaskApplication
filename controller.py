from flask import Flask, redirect, render_template, url_for, session, request
from views import show_form, process_form, experience, save_data, mailing_list, mailing_list_data, summary

app = Flask(__name__)
app.secret_key = "123123"  # Set a secret key for session encryption

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/personalInfo", methods=["GET"])
def show_form_route():
    return show_form()


@app.route("/", methods=["POST"])
def process_form_route():
    return process_form()

@app.route("/experience", methods=["GET"])
def experience_route():
    return experience()

@app.route("/experience", methods=["POST"])
def save_data_route():
    return save_data()

@app.route("/mailingList", methods=["GET"])
def mailing_list_route():
    return mailing_list()

@app.route("/mailingList", methods=["POST"])
def mailing_list_data_route():
    return mailing_list_data()

@app.route("/summary", methods=["GET"])
def summary_route():
    return summary()

if __name__ == "__main__":
    app.run(debug=True)
