from app import db
from datetime import datetime

class Languages(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def to_json(model):
        return {
            'id': model.id,
            'name': model.name
        }