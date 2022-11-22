from app.models.authors import Authors
from app import db

class AuthorRepositoryImplementation():

    def find_by_name(self, author_name):
        author = Authors.query.filter_by(full_name= author_name).first()
        return Authors.to_json(author)


    def find_or_create(self, author_name):
        author = Authors.query.filter_by(full_name=author_name).first()
        if author:
            return Authors.to_json(author)
        else:
            try:
                author_instance = Authors(full_name=author_name)
                db.session.add(author_instance)
                db.session.commit()
                return Authors.to_json(author_instance)
            except Exception:
                db.session.rollback()
                raise Exception("Error while inserting author data.")

