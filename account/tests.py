import json

from django.test import TestCase
from django.test import Client

from account.models import User


class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        user = User(
            email='test@test.com',
            username='test'
        )
        user.set_password('1234')
        user.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_user_signup_success(self):
        """ 유저 회원가입 """
        response = self.client.post(
            '/api/account/signup',
            json.dumps({
                'email': 'test_1@test.com',
                'username': 'test',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        # todo 악성 이메일 데이터 (길이, 변조등) 체크
        self.assertEqual(response.json()['data']['account']['email'], 'test_1@test.com')
        self.assertFalse(response.json()['data']['account']['is_superuser'])
        self.assertTrue(response.json()['data']['account']['is_active'])

    def test_user_login_success(self):
        """ 유저 로그인 """
        response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.json(), {'code': 200, 'message': 'success'})
        self.assertEqual(response.status_code, 200)

    def test_user_logout_success(self):
        """ 유저 로그아웃 """
        login_response = self.client.post(
            '/api/account/login',
            json.dumps({
                'email': 'test@test.com',
                'password': '1234'
            }),
            content_type='application/json'
        )
        self.assertEqual(login_response.status_code, 200)

        logout_response = self.client.post('/api/account/logout', follow=True)
        self.assertEqual(logout_response.status_code, 200)
