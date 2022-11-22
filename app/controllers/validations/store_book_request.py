from marshmallow import Schema, fields

class StoreBookRequestValidator(Schema):
    name = fields.Str(required=True)
    quantity = fields.Integer(required=True, strict=True)
    authors = fields.Str(required=True)
    average_rating = fields.Str(required=True)
    isbn = fields.Str(required=True)
    isbn13 = fields.Str(required=True)
    language_code = fields.Str(required=True)
    publication_date = fields.Str(required=True)
    publisher = fields.Str(required=True)