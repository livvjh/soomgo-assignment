from django.urls import path

from product.views import ProductAPI, PurchaseAPI, PurchaseDetailAPI

urlpatterns = [
    path('', ProductAPI.as_view()),
    path('<int:purchase_id>', PurchaseDetailAPI.as_view()),
    path('purchase', PurchaseAPI.as_view()),
]
