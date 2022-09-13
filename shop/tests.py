from django.contrib.auth.models import User
from django.test import TestCase

from shop.models import *


class TestDataBase(TestCase):
    # fixtures = [
    #     'shop/fixtures/mydata.json'
    # ]

    # def setUp(self):
    #     self.user = User.objects.get(username='user')
    #
    # def test_user_exists(self):
    #     users = User.objects.all()
    #     users_number = users.count()
    #     user = users.first()
    #     self.assertEqual(users_number, 1)
    #     self.assertEqual(user.username, 'user')
    #     self.assertTrue(user.is_superuser)
    #
    # def test_user_check_password(self):
    #     self.assertTrue(self.user.check_password('1234'))

    def find_cart_number(self):
        cart_number = Order.objects.filter(user=self.user,
                                           status=Order.STATUS_CART).count()
        return cart_number

    def test_function_get_cart(self):


        # No cart
        self.assertEqual(self.find_cart_number(), 0)

        # Create cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)

        # Get created cart
        Order.get_cart(self.user)
        self.assertEqual(self.find_cart_number(), 1)



