"""
Application file for Flask app sim-exchange-backend.

Flask view function names should correspond 1:1 with their respective 
.html file names within the app/templates directory.
"""
import os
from flask import (
    Flask,
    render_template,
    make_response,
    session,
    redirect,
    url_for,
    request,
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_required,
    fresh_login_required,
    login_user,
    logout_user,
    UserMixin,
)
from werkzeug.security import generate_password_hash, check_password_hash
#from models import User
#from dbconfig import DATABASE_URI

# login/logout

login_manager = LoginManager()
login_manager.session_protection = "strong"


def create_app():
    app = Flask(__name__)
    #app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    # generate random session key
    app.secret_key = os.urandom(16)

    #from models import db

    #db.init_app(app)
    #login_manager.init_app(app)
    return app


app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

