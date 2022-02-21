from django.urls import path
from account.views import SignUpAPI, LogOutAPI, LogInAPI

urlpatterns = [
    path('login', LogInAPI.as_view()),
    path('signup', SignUpAPI.as_view()),
    path('logout', LogOutAPI.as_view()),
]
