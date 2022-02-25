from drf_yasg import openapi


def create_openapi(parameter_key: str, parameter_type: str, required: bool, description: str,
                   parameter_location: str = openapi.IN_QUERY):
    return openapi.Parameter(
        name=parameter_key,
        in_=parameter_location,
        description=description,
        required=required,
        type=parameter_type
    )
