from unittest import TestCase
from django.urls import resolve
from product.models import (
    Product,
    Purchase,
    Category
)
from product.views import ProductAPI


class UserTest(TestCase):
    def setUp(self):
        # user가 무적권 있어야함
        pass

    def tearDown(self):
        pass

    def test_product_list_request_url_exists(self):
        found_url = resolve('/api/product/')
        self.assertEqual(found_url.func.view_class, ProductAPI)

    def test_admin_create_product(self):
        """ 관리자 상품 등록 """
        pass

    def test_buy_product(self):
        """ 상품 구매 """
        pass

    def test_proudct_detail(self):
        """ 상품 상세 """
        pass

    def test_proudct_list(self):
        """ 상품 목록 """
        pass
