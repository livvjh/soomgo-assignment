from django.contrib import admin
from .models import User


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'last_login',
        'date_joined'
    ]


admin.site.register(User, AccountAdmin)
