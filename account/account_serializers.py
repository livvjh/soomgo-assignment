from rest_framework import serializers

from account.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'last_login',
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined'
        ]


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password'
        ]
