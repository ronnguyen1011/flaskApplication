from flask import Flask, redirect, render_template, url_for, session, request

app = Flask(__name__)
app.secret_key = "123123"  # Set a secret key for session encryption

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/personalInfo", methods=["GET"])
def show_form():
    return render_template("personalInfo.html")


@app.route("/", methods=["POST"])
def process_form():
    # Access the form data using request.form
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")
    state = request.form.get("state")
    phone = request.form.get("phone")
    ml_signup = bool(request.form.get("MLSignUp"))

    # Store the form data in the session
    session["first_name"] = first_name
    session["last_name"] = last_name
    session["email"] = email
    session["state"] = state
    session["phone"] = phone
    session["ml_signup"] = ml_signup
    return redirect(url_for("experience"))


@app.route("/experience", methods=["GET"])
def experience():
    return render_template("experience.html")


@app.route("/experience", methods=["POST"])
def saveData():
    biography = request.form.get("biography")
    gitLink = request.form.get("gitLink")
    year = request.form.get("fav_language")
    experience = request.form.get("fav_language1")
    session["biography"] = biography
    session["gitLink"] = gitLink
    session["fav_language"] = year
    session["fav_language1"] = experience
    return redirect(url_for("mailingList"))


@app.route("/mailingList", methods=["GET"])
def mailingList():
    return render_template("mailingList.html")


@app.route("/mailingList", methods=["POST"])
def mailingListData():
    jobs = request.form.getlist("Jobs")
    industry = request.form.getlist("Industry")
    session["jobs"] = jobs
    session["Industry"] = industry

    return redirect(url_for("summary"))


@app.route("/summary", methods=["GET"])
def summary():
    first_name = session.get("first_name")
    last_name = session["last_name"]
    email = session["email"]
    state = session["state"]
    phone = session["phone"]
    gitlink = session["gitLink"]
    bio = session["biography"]
    jobs = session["jobs"]
    industry = session["Industry"]
    year = session["fav_language"]
    experience = session["fav_language1"]
    return render_template(
        "summary.html",
        first_name=first_name,
        last_name=last_name,
        email=email,
        state=state,
        phone=phone,
        gitlink=gitlink,
        bio=bio,
        jobs=jobs,
        industry=industry,
        year=year,
        experience=experience,
    )


if __name__ == "__main__":
    app.run(debug=True)
