from flask import Blueprint, render_template,request,session,redirect

home_controller = Blueprint('home_controller', __name__)
@home_controller.route('/')
def home():
    # Fetch users from the database

    # Render the home template and pass the users as context
    return render_template('home.html')

@home_controller.route('/personalInfo', methods=['GET', 'POST'])
def personalInfo():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        state = request.form.get('state')
        phone = request.form.get('phone')
        ml_signup = bool(request.form.get('MLSignUp'))

    # Store the form data in the session
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['email'] = email
        session['state'] = state
        session['phone'] = phone
        session['ml_signup'] = ml_signup
        return redirect('/mailingList')
    print(session.get('first_name'))    
    
    return render_template('personalInfo.html')

@home_controller.route('/experience')
def experience():
    first_name = session.get('first_name')
    return render_template('experience.html',first_name=first_name)


@home_controller.route('/mailingList')
def mailingList():
    return render_template('mailingList.html')

@home_controller.route('/summary')
def summary():
    fname = session.get('first_name')
    return render_template('summary.html',fname=fname)