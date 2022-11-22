from app import db
from app.models.publishers import Publisher

class PublisherRepositoryImplementation():

    def find_by_name(self, publisher_name):
        publisher_instance = Publisher.query.filter_by(full_name=publisher_name).first()
        return Publisher.to_json(publisher_instance)


    def find_or_create(self, publisher_name):
        publisher_instance = Publisher.query.filter_by(full_name=publisher_name).first()
        if publisher_instance:
            return Publisher.to_json(publisher_instance)
        else:
            try:
                publisher_instance = Publisher(full_name=publisher_name)
                db.session.add(publisher_instance)
                db.session.commit()
                return Publisher.to_json(publisher_instance)
            except Exception:
                db.session.rollback()
                raise Exception("Error while inserting publisher data.")


