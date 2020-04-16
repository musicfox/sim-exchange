from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    A user in the database.

    Extremely basic setup for PostgreSQL user with 
    password setting capabilities.

    Attributes:
    ===========
    id: primary SQL index integer key
    email: string email; required
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('permission denied: password (read)')

    @password.setter
    def password(self, password):
        """
        Using workzeug, generate a hash given the password.
        Add and commit. 
        """
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        """
        Using werkzeug, check the hash for the password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email}>"
