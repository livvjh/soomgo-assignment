import json

from django.test import TestCase
from django.test import Client
from django.urls import resolve

from account.models import User
from product.models import (
    Product,
    Purchase,
    Category
)
from product.views import ProductAPI


class ProductTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_id = None
        self.purchase_id = None
        self.product_id = None

        user_data_list = [
            {
                'email': 'test_super@test.com',
                'username': 'super'
            },
            {
                'email': 'test@test.com',
                'username': 'test'
            }
        ]
        category_data_list = [
            {
                'name': '홈 인테리어',
                'parent_category_id': None,
            }, {
                'name': '페인트 시공',
                'parent_category_id': 1,
            }, {
                'name': '집 인테리어',
                'parent_category_id': 1,
            }, {
                'name': '싱크대 교체',
                'parent_category_id': 1,
            }, {
                'name': '이벤트',
                'parent_category_id': None,
            }, {
                'name': '결혼식 사회자',
                'parent_category_id': 5,
            }, {
                'name': '웨딩사진촬영',
                'parent_category_id': 5,
            }, {
                'name': '개발',
                'parent_category_id': None,
            }, {
                'name': '앱 디자인',
                'parent_category_id': 11,
            }, {
                'name': '소프트웨어 개발',
                'parent_category_id': 11,
            }
        ]
        for user_data in user_data_list:
            user = User(
                email=user_data['email'],
                username=user_data['username']
            )
            user.set_password('1234')
            if user_data['username'] == 'super':
                user.is_superuser = True
            user.save()

        for category_data in category_data_list:
            category = Category(name=category_data['name'])
            category.save()

            if not category.parent_category_id is None:
                category.parent_category_id = category_data['parent_category_id']
            category.save(update_fields=['parent_category_id'])

        product = Product.objects.create(
            category_id=3,
            name="상품 test",
            price=10000,
            description="상품 test 설명",
        )
        self.product_id = product.id
        self.user_id = User.objects.get(email=user_data_list[0]['email']).pk
        purchase = Purchase.objects.create(
            product_id=self.product_id,
            user_id=self.user_id
        )
        self.purchase_id = purchase.pk

    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Purchase.objects.all().delete()

    def test_product_list_request_url_exists(self):
        found_url = resolve('/api/product/')
        self.assertEqual(found_url.func.view_class, ProductAPI)

    def test_admin_create_product(self):
        """ 관리자 상품 등록 """
        login_response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test_super@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(login_response.status_code, 200)

        input_data = {
            'category_id': 4,
            'name': "상품-1",
            'price': 100,
            'description': "상품-1은 최첨단입니다."
        }

        self.assertTrue(input_data['price'] > 0)

        product = Product.objects.create(
            category_id=input_data['category_id'],
            name=input_data['name'],
            price=input_data['price'],
            description=input_data['description'],
        )
        check_200_data = {
            'category_id': product.category_id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        }
        self.assertEqual(check_200_data, input_data)

    def test_buy_product(self):
        """ 상품 구매 """
        login_response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(login_response.status_code, 200)
        product_id_set = [self.product_id]
        purchase_response = self.client.post(
            '/api/product/purchase',
            json.dumps({
                'product_id_set': product_id_set
            }),
            content_type='application/json'
        )

        self.assertEqual(purchase_response.status_code, 200)

    def test_product_detail(self):
        """ 상품 상세 """
        login_response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(login_response.status_code, 200)

        response = self.client.get(
            '/api/product/',
            {'purchase_id': self.purchase_id}
        )
        self.assertEqual(response.status_code, 200)

    def test_product_list(self):
        """ 구매 상품 목록 """
        login_response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(login_response.status_code, 200)

        response = self.client.get(
            '/api/product/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['purchase_list'], [])
