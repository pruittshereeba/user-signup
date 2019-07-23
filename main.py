from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/register", methods=["POST", "GET"])
def register():

    user_name = ''
    password = ''
    verify_password = ''
    email = ''
    space = ' '

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    if request.method == "POST":

        user_name = request.form['user_name']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']
        
        if len(user_name) < 3 or len(user_name) > 20 and user_name.count(space) == 0:
            username_error = "Please enter a username between 3 and 20 characters."
            user_name = ''
        

        if len(password) < 3 or len(password) > 20 or password == 0:
            password_error = "Please enter a password between 3 and 20 characters/password cannot contain spaces."
            password = ''

        if verify_password != password:
            verify_password_error = "Passwords do not match."
            verify_password = ''

        if len(email) < 3 or len(email) > 20 and "@" or "." not in (email):
            email_error = "Please enter a valid email address. "
            email = ''
            
        if not username_error and not password_error and not verify_password_error and not email_error:
            user_name = request.form['user_name']
            return redirect('/welcome?user_name={0}'.format(user_name))

    
    return render_template('/register.html', title="Fix Errors", user_name=user_name, password=password, verify_password=verify_password, 
            email=email, username_error=username_error, password_error=password_error,
            verify_password_error=verify_password_error, email_error=email_error)

@app.route('/welcome', methods=["GET"])
def welcome():
    title = "Welcome!"
    user_name = request.args.get('user_name')
    return render_template('welcome.html', title="Success", user_name=user_name)


__name__ = "__main__"
app.run()
