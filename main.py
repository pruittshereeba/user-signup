from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup-page.html', username=username, password=password, verify_password=verify_password, 
    email=email)


def is_valid_email(email):
    if len(email) < 3 or len(email) > 20:
        return False

    at = "@"
    at_count = email.count(at)
    if at_count != 1:
        return False

    period = "."
    period_count = email.count(period)
    if period_count != 1:
        return False

    space = " "
    space_count = email.count(space)
    if space_count != 0:
        return False

    else:
        return True

@app.route("/signup-page.html", methods=['POST', 'GET'])
def register():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    space = ' '


    if len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters."
        username = ''

    if username.count(space) != 0:
        username_error = "Please enter a username between 3 and 20 characters."
        username= ''        

    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters."
        password = ''

    if password.count(space) != 0:
        password_error = "Password cannot contain spaces."
        password = ''

    if verify_password != password:
        verify_password_error = "Passwords do not match."
        verify_password = ''

    if len(email) != 0:
        if is_valid_email(email) == False:
            email_error = "Please enter a valid email."
            email = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = request.form['username']
        return redirect('/welcome?username={}'.format(username))

    else:
        return render_template('/signup-page.html', title="Sign-up Page", username=username, email=email,
            username_error=username_error, password_error=password_error,
            verify_password_error=verify_password_error, email_error=email_error)

@app.route('/welcome.html', methods=['GET', 'POST'])
def welcome():
    title = "Welcome!"
    username = request.args.get('username')
    return render_template('welcome.html', title="Success", username=username)


app.run()
