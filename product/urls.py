from django.urls import path

from product.views import ProductAPI

urlpatterns = [
    path('', ProductAPI.as_view(), name='todo_index'),
]
