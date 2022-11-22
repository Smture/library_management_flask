from app import db
from datetime import datetime

class Result(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    status = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def __init__(self, name, status):
        self.name = name
        self.status = status
