from app import db
from datetime import datetime

class Members(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    status = db.Column(db.String(64))
    currently_issued_book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    past_due_or_fine = db.Column(db.Float)
    book_amount = db.Column(db.Float)
    total_payable_amount = db.Column(db.Float)
    remarks = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'currently_issued_book_id': self.currently_issued_book_id,
            'past_due_or_fine': self.past_due_or_fine,
            'book_amount': self.book_amount,
            'total_payable_amount': self.total_payable_amount,
            'remarks': self.remarks,
        }

    # def __init__(self, name, status, currently_issued_book_id, past_due_or_fine, book_amount, total_payable_amount, remarks):
    #     self.name = name
    #     self.status = status
    #     self.currently_issued_book_id = currently_issued_book_id
    #     self.past_due_or_fine = past_due_or_fine
    #     self.book_amount = book_amount
    #     self.total_payable_amount = total_payable_amount
    #     self.remarks = remarks

