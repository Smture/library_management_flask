from app import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    email_id = db.Column(db.String(64), unique=True,nullable=False)
    status = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    user_name = db.Column(db.String(20), nullable = False, unique=True)
    password = db.Column(db.String(64), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def __init__(self, email_id, user_name, password):
        self.email_id = email_id
        self.user_name = user_name
        self.password = password