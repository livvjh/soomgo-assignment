from django.contrib import auth
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema, no_body
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


class LogInAPI(APIView):
    """ 유저 로그인 """
    permission_classes = ()
    authentication_classes = ()

    @swagger_auto_schema(tags=['로그인 API'], request_body=LogInSerializer, responses={200: 'success'})
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
    authentication_classes = ()

    @swagger_auto_schema(tags=['회원가입 API'], request_body=SignUpSerializer, responses={200: 'success'})
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
    @swagger_auto_schema(tags=['로그아웃 API'], request_body=no_body, responses={200: 'success'})
    def post(self, request):
        logout(request)
        return Response(response_serializer(STATUS_SUCCESS), status=status.HTTP_200_OK)