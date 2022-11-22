from injector import inject
from app.repositories.language.language_repository import LanguageRepository

class LanguageService:
    @inject
    def __init__(self, language_repository: LanguageRepository):
        self.language_repository = language_repository


    def find_by_name(self, language_code):
        return self.language_repository.find_by_name(language_code)


    def find_or_create(self, language_code):
        return self.language_repository.find_or_create(language_code)