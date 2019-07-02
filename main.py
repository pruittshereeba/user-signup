from flask import Flask, request, render_template, redirect
import re

app=Flask(__name__)

app.config['DEBUG']=True







    @app.route('/', methods=['POST','GET'])
    def home_screen():
        if request.method == 'POST':
            user_name = request.form['user_name']
            password = request.form['password']
            verify_password = request.form['verify_password']
            email = request.form['email']
            
            user_name_error=""
            password_error=""
            verify_pass_error=""
            compare_pass_error=""
            email_error=""

            user_name_error= validate(user_name).format(name="Username")
            password_error = validate(password).format(name="Password")
            verify_pass_error = validate(verify_password).format(name="Verify Password")

            #compares password to verify password
            if verify_password not in password:
                compare_pass_error="Sorry, those don't match, try again please!"
            #check email input
            if email:
                if not re.search(r"([a-z]+[@]+[a-z]+[.]+[a-z])", email):
                    email_error="Please enter a valid email address: "
                else:
                    email_error = validate(email).format(name="Email")
            if not (user_name_error or
                    password_error or
                    verify_pass_error or
                    compare_pass_error or
                    email_error
                    ):
                    return redirect('welcome?user_name={0}'.format(user_name))
            return render_template('signup-page.html',
                                    user_name_error=user_name_error,
                                    password_error=password_error,
                                    verify_pass_error=verify_pass_error,
                                    compare_pass_error=compare_pass_error,
                                    email_error=email_error,
                                    user_name=user_name,
                                )
        return render_template('signup-page.html', title="User Sign Up Page")
@app.route('/welcome')
def welcome_user():
    user_name=request.args.get('user_name')
    return render_template('welcome.html', user_name=user_name)

app.run()
