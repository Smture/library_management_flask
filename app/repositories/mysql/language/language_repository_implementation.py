from app import db
from app.models.languages import Languages

class LanguageRepositoryImplementation():

    def find_by_name(self, language_code):
        language_instance = Languages.query.filter_by(name=language_code).first()
        return Languages.to_json(language_instance)


    def find_or_create(self, language_code):
        language = Languages.query.filter_by(name=language_code).first()
        if language:
            return Languages.to_json(language)
        else:
            try:
                language_instance = Languages(name=language_code)
                db.session.add(language_instance)
                db.session.commit()
                return Languages.to_json(language_instance)
            except Exception:
                db.session.rollback()
                raise Exception("Error while inserting language data.")