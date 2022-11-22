from app import db
from datetime import datetime

class Authors(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def to_json(model):
        return {
            'id': model.id,
            'full_name': model.full_name
        }
