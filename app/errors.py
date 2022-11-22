# class Errors:
#     string_type_error = "value must be of type string."
#     int_type_error = "value must be of type integer."
#     bool_type_error = "value must be of type boolean"
#     integrity_violation_error = "record already exists."
#     empty_value_error = "value must not be empty."


class Errors:
    @staticmethod
    def string_type_error(value):
        string_type_error = value + " value must be of type string."
        return string_type_error


    @staticmethod
    def int_type_error(value):
        int_type_error = value + " value must be of type integer."
        return int_type_error


    @staticmethod
    def bool_type_error(value):
        bool_type_error = value + " value must be of type boolean"
        return bool_type_error


    @staticmethod
    def integrity_violation_error(value):
        integrity_violation_error = value + " record already exists."
        return integrity_violation_error


    @staticmethod
    def empty_value_error(value):
        empty_value_error = value + " value must not be empty."
        return empty_value_error

