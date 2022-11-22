from app.errors import Errors

class APIExceptions(Exception):
    def __init__(self, status_code, payload):
        self.status_code =  status_code
        self.payload = payload

    def integrityViolation(Exception):
        status_code = 500
        custom_error = Errors.integrity_violation_error
        error_dict = {
            'status_code': status_code,
            'error': custom_error
        }
        print(error_dict)



