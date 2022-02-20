from django.contrib.auth import logout
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from config.common.exception_handler import CustomAPIException
from config.common.library_classes import response_serializer

from rest_framework import status

from config.common.response_code import MSG_RSP_SUCCESS


class SignInAPI(APIView):
    def post(self, request):
        raise CustomAPIException(
            MSG_RSP_SUCCESS,
            status.HTTP_200_OK
        )
        return Response({'data': 'data'}, status=200)


class SignUpAPI(APIView):
    def post(self, request):
        pass


class SignOutAPI(APIView):
    def post(self, request):
        logout(request)
        # pass
        # return Response(response_serializer(STATUS_RSP_SUCCESS), status=200)
