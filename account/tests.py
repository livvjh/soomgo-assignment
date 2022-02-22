from unittest import TestCase
from django.test import Client

from account.account_serializers import AccountSerializer
from account.models import User

client = Client()  # client는 requests나 httpie가 일하는 방식과 같이 동작


class UserTest(TestCase):
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")

    @staticmethod
    def tearDownClass():
        User.objects.get(email='test_1@test.com').delete()

    # user create
    # def test_create_user(self):
    #     user = User.objects.create_user(
    #         email='test_1@test.com',
    #         password='1234'
    #     )
    #     self.assertEqual(user.email, 'test_1@test.com')
    #     self.assertFalse(user.is_superuser)
    #     self.assertTrue(user.is_active)

    def test_user_signup_success(self):
        response = client.post(
            '/api/account/signup',
            data={
                'email': 'test_1@test.com',
                'username': 'test',
                'password': '1234'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['account']['email'], 'test_1@test.com')
        self.assertEqual(response.json()['data']['account']['username'], 'test')
        """ 유저 회원가입 """

    def test_user_login_success(self):
        """ 유저 로그인 """
        pass
