from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class CustomAPIException(APIException):
    status_code = 200

    def __init__(self, msg, status_code=None):
        self.detail = msg
        if status_code is not None:
            self.status_code = status_code