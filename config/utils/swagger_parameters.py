from drf_yasg import openapi


def create_open_api(parameter_key: str, parameter_type: str, description: str, required: bool):
    if parameter_type == 'str':
        type_value = openapi.TYPE_STRING
    elif parameter_type == 'int':
        type_value = openapi.TYPE_INTEGER
    elif parameter_type == 'arr':
        type_value = openapi.TYPE_ARRAY
    elif parameter_type == 'bool':
        type_value = openapi.TYPE_BOOLEAN

    return openapi.Parameter(
        parameter_key,
        openapi.IN_BODY,
        description=description,
        required=required,
        type=type_value
    )
