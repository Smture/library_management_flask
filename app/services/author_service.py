import logging
from app.repositories.author.author_repository import AuthorRepository
from injector import inject

class AuthorService:
    @inject
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository


    def find_by_name(self, author_name):
        return self.author_repository.find_by_name(author_name)


    def find_or_create(self, author_name):
        return self.author_repository.find_or_create(author_name)


