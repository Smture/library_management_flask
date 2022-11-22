from flask import Response
import json
from http import HTTPStatus

class RestResponse:
    def failure_response(status_code, payload):
        data = {"success": False, "payload": payload}
        data_json = json.dumps(data)

        return Response(data_json, status_code)


    def success_response(payload):
        data = {"success": True, "payload": payload}
        data_json = json.dumps(data)

        return Response(data_json, HTTPStatus.OK)


    def permission_denied(message):
        data = {"success": False, "payload": message}
        data_json = json.dumps(data)

        return Response(data_json, HTTPStatus.UNAUTHORIZED)