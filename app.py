from flask import Flask, redirect, render_template, url_for, session, request

app = Flask(__name__)
app.secret_key = "123123"  # Set a secret key for session encryption


@app.route("/", methods=["GET"])
def show_form():
    return render_template("personalInfo.html")


@app.route("/", methods=["POST"])
def process_form():
    # Access the form data using request.form
    name = request.form.get("fname")
    session["data"] = name
    return redirect(url_for("experience"))


@app.route("/experience", methods=["GET"])
def experience():
    return render_template("experience.html")


@app.route("/experience", methods=["POST"])
def saveData():
    name = session.get("data")
    return redirect(url_for("mailingList"))


@app.route("/mailingList", methods=["GET"])
def mailingList():
    return render_template("mailingList.html")


@app.route("/mailingList", methods=["POST"])
def mailingListData():
    return redirect(url_for("summary"))


@app.route("/summary", methods=["GET"])
def summary():
    data = session.get("data")
    return render_template("summary.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
