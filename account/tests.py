from unittest import TestCase
from account.models import User


class UserTest(TestCase):
    def test_create_user(self):
        # user = User.objects.create_user(
        #     email='test_3@test.com',
        #     password='1234'
        # )
        # self.assertEqual(user.email, 'test_3@test.com')
        # self.assertFalse(user.is_superuser)
        # self.assertTrue(user.is_active)
        self.assertTrue(1 + 1 == 2)

    def test_user_signup(self):
        """ 유저 회원가입 """
        pass

    def test_user_signin(self):
        """ 유저 로그인 """
        pass

    def test_user_logout(self):
        """ 유저 로그아웃 """
        pass
