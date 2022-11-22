from dataclasses import dataclass

@dataclass
class BookDTO:
    name: str
    author_id: int
    average_rating: str
    isbn: str
    isbn13: str
    language_id: int
    publication_date: str
    publisher_id: int

    # get age
    def get_name(self):
        return self.name

    # set age
    def set_name(self, name):
        self.name = name

    # get author_id
    def get_author_id(self):
        return self.author_id

    # set author_id
    def set_author_id(self, author_id):
        self.author_id = author_id

    # get average_rating
    def get_average_rating(self):
        return self.average_rating

    # set average_rating
    def set_average_rating(self, average_rating):
        self.average_rating = average_rating

    # get isbn
    def get_isbn(self):
        return self.isbn

    # set isbn
    def set_isbn(self, isbn):
        self.isbn = isbn

    # get isbn13
    def get_isbn13(self):
        return self.isbn13

    # set isbn13
    def set_isbn13(self, isbn13):
        self.isbn13 = isbn13

    # get language_id
    def get_language_id(self):
        return self.language_id

    # set language_id
    def set_language_id(self, language_id):
        self.language_id = language_id

    # get publication_date
    def get_publication_date(self):
        return self.publication_date

    # set publication_date
    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    # get publisher_id
    def get_publisher_id(self):
        return self.publisher_id

    # set publisher_id
    def set_publisher_id(self, publisher_id):
        self.publisher_id = publisher_id


