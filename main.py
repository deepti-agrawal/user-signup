from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html',username="",email="",username_error="",password_error="",verify_error="", email_error="", title="User Signup")

@app.route("/signup",methods=['POST'])
def sign_up():
    EMAIL_REGEX = re.compile("[^@]+@[^@]+\.[^@]+")
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']
    username_error_message = ""
    password_error_message = ""
    verify_error_message = ""
    email_error_message = ""
    if username == "" or len(username)<3 or len(username)>20 or ' ' in username:
        username_error_message = "That's not a valid username"
        username=''
    if password == "" or len(password)<3 or len(password)>20 or ' ' in password:
        password_error_message = "That's not a valid password"
        password=''
    if verify_password == "" or len(verify_password)<3 or len(verify_password)>20 or ' ' in verify_password or password != verify_password:
        verify_error_message = "Password don't match!"
        verify_password=''
    if email != "" and (len(email)<3 or len(email)>20 or ' ' in email or not EMAIL_REGEX.match(email)):
        email_error_message = "This is not valid email!"
        email=''
    if not username_error_message and not password_error_message and not verify_error_message and not email_error_message:
        return render_template('welcome.html', title="Welcome",username=cgi.escape(username))
    else:
        return render_template('index.html', title="User Signup", username=username, email=email, username_error=username_error_message, password_error=password_error_message, verify_error=verify_error_message, email_error=email_error_message)

app.run()