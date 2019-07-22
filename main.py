from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup-page", methods=['POST', 'GET'])
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

    user_name = request.form["user_name"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    if request.method == "POST":
        return "Hello"  


        if len(user_name) < 3 or len(user_name) > 20 or user_name.count(space) != 0 or len(password) < 3 or len(password) > 20:
            username_error = "Please enter a user_name between 3 and 20 characters."
            user_name = ''

        elif user_name.count(space) != 0:
            username_error = "Please enter a user_name between 3 and 20 characters."
            user_name= ''        

        # if len(password) < 3 or len(password) > 20:
        #     password_error = "Please enter a password between 3 and 20 characters."
        #     password = ''

        # if password.count(space) != 0:
        #     password_error = "Password cannot contain spaces."
        #     password = ''

        # if verify_password != password:
        #     verify_password_error = "Passwords do not match."

        #     verify_password = ''

        # if len(email) != 0:
        #     if is_valid_email(email) == True:
        #         email_error = "Please enter a valid email."
        #         email = ''
            

        if not username_error and not password_error and not verify_password_error and not email_error:
            #user_name = request.form['user_name']
            #return "Hello"
            return redirect('/welcome?user_name={0}'.format(user_name))

        else:
            return render_template('/signup-page.html', title="Fix Errors", username_error=username_error, password_error=password_error,
            verify_password_error=verify_password_error, email_error=email_error)

    
    return render_template('signup-page.html')

@app.route('/welcome', methods=['GET'])
def welcome():
    title = "Welcome!"
    #user_name = request.args.get('user_name')
    return render_template('welcome.html', title="Success", user_name=user_name)


__name__ = "__main__"
app.run()
