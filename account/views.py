from django.contrib import auth
from django.contrib.auth import logout, login
from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from account.account_serializers import AccountSerializer, SignUpSerializer, LogInSerializer
from account.models import User
from config.common.exception_handler import CustomAPIException
from config.common.library_classes import response_serializer, essential_param

from rest_framework import status

from config.common.response_code import (
    STATUS_SUCCESS,
    MSG_RSP_USER_NOT_MATCHED,
    MSG_RSP_USER_EMAIL_ALREADY_EXISTS
)
from config.utils.swagger_parameters import create_open_api


class LogInAPI(APIView):
    """ 유저 로그인 """
    email = create_open_api('email', 'str', '이메일(ID)을 입력하세요.', True)
    password = create_open_api('password', 'str', '비밀번호를 입력하세요.', True)

    @swagger_auto_schema(tags=['로그인 API'], request_body=LogInSerializer, responses={200: 'Success'})
    def post(self, request):
        email = essential_param(request, 'email')
        password = essential_param(request, 'password')
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            raise CustomAPIException(
                MSG_RSP_USER_NOT_MATCHED,
                500
            )
        return Response(response_serializer(STATUS_SUCCESS), status=status.HTTP_200_OK)


class SignUpAPI(APIView):
    """ 유저 회원가입 """
    permission_classes = ()

    email = create_open_api('email', 'str', '이메일(ID)을 입력하세요.', True)
    password = create_open_api('password', 'str', '비밀번호를 입력하세요.', True)
    username = create_open_api('username', 'str', '유저명을 입력하세요.', True)

    @swagger_auto_schema(tags=['회원가입 API'], request_body=SignUpSerializer, responses={200: 'Success'})
    def post(self, request):
        email = essential_param(request, 'email')
        username = essential_param(request, 'username')
        password = essential_param(request, 'password')
        try:
            user = User.objects.create(email=email, username=username)
        except IntegrityError:
            raise CustomAPIException(
                MSG_RSP_USER_EMAIL_ALREADY_EXISTS,
                500
            )
        user.set_password(password)
        user.save()
        login(request, user)
        context = {
            'account': AccountSerializer(user).data
        }
        return Response(response_serializer(STATUS_SUCCESS, context), status=status.HTTP_200_OK)


class LogOutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response(response_serializer(STATUS_SUCCESS), status=status.HTTP_200_OK)
