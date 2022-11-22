import logging
from injector import inject
import logging

from app.repositories.book.book_repository import BookRepository

from app.services.author_service import AuthorService
from app.services.language_service import LanguageService
from app.services.publisher_service import PublisherService

from app.DTO.Book.book_dto import BookDTO

class BookService:
    @inject
    def __init__(self,
                 book_repository: BookRepository,
                 author_service: AuthorService,
                 language_service: LanguageService,
                 publisher_service: PublisherService):

        self.book_repository = book_repository
        self.author_service = author_service
        self.language_service = language_service
        self.publisher_service = publisher_service

    def store(self, validated_request_data):

        book_creation_response = []
        logging.info("Looping through request data.")
        for i in validated_request_data:

            author_name = i['authors']
            logging.info("Finding author by name or creating one if not found.")
            author = self.author_service.find_or_create(author_name)
            if not author:
                raise Exception("Error while processing author details.")
            author_id = author['id']


            language_code = i['language_code']
            logging.info("Finding language by name or creating one if not found.")
            language = self.language_service.find_or_create(language_code)

            if not language:
                raise Exception("Error while processing language details.")
            language_id = language['id']


            publisher_name = i['publisher']
            logging.info("Finding publisher by name or creating one if not found.")
            publisher = self.publisher_service.find_or_create(publisher_name)
            if not language:
                raise Exception("Error while processing publisher details.")
            publisher_id = publisher['id']


            logging.info("Setting DTO.")
            book_dto = BookDTO(
                name = i['name'],
                author_id = author_id,
                average_rating = i['average_rating'],
                isbn = i['isbn'],
                isbn13 = i['isbn13'],
                language_id = language_id,
                publication_date = i['publication_date'],
                publisher_id = publisher_id
                )


            book_creation_response.append(self.book_repository.store(book_dto))

        return book_creation_response