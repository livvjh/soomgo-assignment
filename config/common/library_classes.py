from rest_framework.exceptions import APIException

from config.common.response_code import code_to_message


def response_serializer(code, data=None):
    json_data = dict()
    json_data['code'] = code
    json_data['message'] = code_to_message(code)
    if data is not None:
        json_data['data'] = data
    return json_data


def essential_param(request, name):
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


def optional_param(request, name, default_value=''):
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
