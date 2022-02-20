from django.urls import path

from account.views import SignInAPI, SignUpAPI, SignOutAPI

urlpatterns = [
    path('signin', SignInAPI.as_view()),
    path('signup', SignUpAPI.as_view()),
    path('signout', SignOutAPI.as_view()),
]
