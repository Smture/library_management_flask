from app import db
from datetime import datetime

class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    average_rating = db.Column(db.String(10), nullable=False)
    isbn = db.Column(db.String(50), unique=True, nullable=False)
    isbn13 = db.Column(db.String(50), unique=True, nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"), nullable=False)
    publication_date = db.Column(db.String(10), nullable=False)
    total_stock = db.Column(db.Integer, default=10)
    total_issued = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def to_json(model):
        return {
            'id': model.id,
            'name': model.name
        }




