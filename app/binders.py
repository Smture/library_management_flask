from injector import singleton

from app.repositories.book.book_repository import BookRepository
from app.repositories.mysql.book.book_repository_implementation import BookRepositoryImplementation

from app.repositories.author.author_repository import AuthorRepository
from app.repositories.mysql.author.author_repository_implementation import AuthorRepositoryImplementation

from app.repositories.publisher.publisher_repository import PublisherRepository
from app.repositories.mysql.publisher.publisher_repository_implementation import PublisherRepositoryImplementation

from app.repositories.language.language_repository import LanguageRepository
from app.repositories.mysql.language.language_repository_implementation import LanguageRepositoryImplementation

#bind the repo and repo implementations
def configure(binder):
    binder.bind(BookRepository, to=BookRepositoryImplementation, scope=singleton)
    binder.bind(AuthorRepository, to=AuthorRepositoryImplementation, scope=singleton)
    binder.bind(PublisherRepository, to=PublisherRepositoryImplementation, scope=singleton)
    binder.bind(LanguageRepository, to=LanguageRepositoryImplementation, scope=singleton)