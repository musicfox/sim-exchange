"""
Application file for Flask app sim-exchange-backend.

Flask view function names should correspond 1:1 with their respective 
.html file names within the app/templates directory.
"""
import os
from flask import (
    Flask, render_template, make_response, session, redirect, url_for, request
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, fresh_login_required, login_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from dbconfig import DATABASE_URI
# login/logout

login_manager = LoginManager()
login_manager.session_protection = "strong"
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    # generate random session key
    app.secret_key = os.urandom(16)

    from models import db
    db.init_app(app)
    login_manager.init_app(app)
    return app

app = create_app()
# define unauthorized access
@login_manager.unauthorized_handler
def unauthorized():
    """
    View for unauthorized access.
    """
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template('index.html')

#@app.route('/investors/login', methods=['GET', 'POST'])
#def login():
#    """
#    The investor login page.
#
#    Investor users are given an email and password.
#    """
#
#    form = InvestorsLoginForm(request.form)
#    if request.method == 'GET':
#        return render_template("investors-login.html", form=form) # no form available
#
#
#    if request.method == 'POST' and form.validate():
#        email = request.form['email']
#        user = User.query.filter_by(email=email).first()
#        psswd = request.form['password']
#
#        if user:
#            if user.verify_password(psswd):
#                login_user(user)
#                session['email'] = email
#                return redirect('/investors')
#            return render_template("investors-login.html", form = form)
#        return render_template("investors-login.html", form = form)
#
#    return render_template("investors-login.html", form = form)
#    
#@app.route('/investors/logout')
#@login_required
#def logout():
#    # remove the email from the session if extant
#    session.pop('email', None)
#    logout_user()
#    return redirect(url_for('landing_page'))
#
#@app.route('/investors')
#@fresh_login_required
#def investors():
#    return render_template("investors.html")
