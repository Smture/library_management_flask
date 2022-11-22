from app.models.books import Books
from app import db

class BookRepositoryImplementation():

    def store(self, book_dto):
        try:
            books_instance = self.data_parser(data=book_dto)
            db.session.add(books_instance)
            db.session.commit()
            return Books.to_json(books_instance)
        except Exception:
            db.session.rollback()
            raise Exception("Error while inserting book data.")

    def fetch(self, data):
        pass


    def find(self, data):
        pass


    def data_parser(self, data):
        book_name = data.get_name()
        author_id = data.get_author_id()
        average_rating = data.get_average_rating()
        isbn = data.get_isbn()
        isbn13 = data.get_isbn13()
        language_id = data.get_language_id()
        publication_date = data.get_publication_date()
        publisher_id = data.get_publisher_id()

        return Books(name=book_name,
                     author_id=author_id,
                     average_rating=average_rating,
                     isbn=isbn,
                     isbn13=isbn13,
                     language_id=language_id,
                     publication_date=publication_date,
                     publisher_id=publisher_id
                     )