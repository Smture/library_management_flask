from app.controllers.book_controller import BookController
from flask import request, Blueprint

api_routes = Blueprint("v1", __name__, url_prefix="/api/v1")


@api_routes.route("/", methods=['GET'])
def fetch_basic_homepage():
    return fetch_homepage()


@api_routes.route("/home", methods=['GET'])
def fetch_homepage():
    return "HOME"


@api_routes.route("/signup", methods=['GET'])
def fetch_signup_page():
    return "SIGNUP"


@api_routes.route("/insert", methods=['POST'])
def insert_data(book_controller: BookController):

    request_data_json = request.json

    return book_controller.store(request_data_json)

