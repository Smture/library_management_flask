from injector import inject
#from app.repositories.book.book_repository import BookRepository
from app.services.book_service import BookService
from app.controllers.validations.store_book_request import StoreBookRequestValidator
from flask import jsonify
from app.exceptions import APIExceptions
from app.rest_responses import RestResponse

class BookController:
    @inject
    def __init__(self, book_service: BookService):
        self.book_service = book_service

    def store(self, insert_request):
        try:
            errors = StoreBookRequestValidator().validate(insert_request, many=True)
            if errors:
                return RestResponse.failure_response(payload=errors, status_code=422)

            validated_request_data = StoreBookRequestValidator(many=True).load(insert_request)

            book_creation_response = self.book_service.store(validated_request_data)
            #book_creation_response =  self.book_repository.store(validated_request_data)
            return jsonify({
                "status": True,
                "data": book_creation_response
            })
        except APIExceptions as e:
            return RestResponse.failure_response(payload=e.payload, status_code=e.status_code)


