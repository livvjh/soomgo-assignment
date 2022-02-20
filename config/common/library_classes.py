from rest_framework.exceptions import APIException

from config.common.response_code import code_to_alert

JSON_CODE = 'code'
JSON_MESSAGE = 'message'
JSON_DATA = 'data'


# 응답 시리얼라이져
def response_serializer(code, data=None):
    json_data = dict()
    json_data[JSON_CODE] = code
    json_data[JSON_MESSAGE] = code_to_alert(code)
    json_data[JSON_DATA] = data
    return json_data


def essential_elem(request, name):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ['', None]:
            raise APIException('missing required field')
        return data
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ['', None]:
                raise APIException('missing required field')
        except:
            raise APIException('missing required field')
    return data


def optional_elem(request, name, default_value=''):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ['', None]:
            data = default_value
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ['', None]:
                data = default_value
        except:
            data = default_value

    return data
