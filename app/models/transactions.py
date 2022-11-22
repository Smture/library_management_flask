from app import db
from datetime import datetime

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(64))
    issued_to_member_id = db.Column(db.Integer, db.ForeignKey("members.id"), nullable=False)
    issued_by_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    total_amount = db.Column(db.Float)
    remarks = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=db.func.now())

    def __init__(self, transaction_id, issued_to_member_id, issued_by_id, total_amount, remarks):
        self.transaction_id = transaction_id
        self.issued_to_member_id = issued_to_member_id
        self.issued_by_id = issued_by_id
        self.total_amount = total_amount
        self.remarks = remarks
