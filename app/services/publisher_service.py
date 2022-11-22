from injector import inject
from app.repositories.publisher.publisher_repository import PublisherRepository

class PublisherService:
    @inject
    def __init__(self, publisher_repository: PublisherRepository):
        self.publisher_repository = publisher_repository


    def find_by_name(self, publisher_name):
        return self.publisher_repository.find_by_name(publisher_name)


    def find_or_create(self, publisher_name):
        return self.publisher_repository.find_or_create(publisher_name)
