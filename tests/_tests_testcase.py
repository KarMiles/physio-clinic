# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.test import TestCase
from django.test import Client
from django.views import generic
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from poll.views import PollList
from poll.models import Poll


User = get_user_model()

# class TestViews(TestCase):
#     '''
#     Test views
#     '''
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass
    
#     def setUp(self):
#         '''
#         Set up testing data
#         '''
#         # Create test user
#         if not User.objects.filter(username='user_staff_test').exists():
#             User.objects.create(
#                 username='user_staff_test',
#                 password='1qazcde3',
#                 is_staff='True'
#             )
#         else:
#             print('Test user already exists, proceeding with test.')

#         # Create test Poll
#         # Poll.objects.create(
#         #     poll_id='999',
#         #     author=User.username,
#         #     question='Which option?',
#         #     option_one='option_one',
#         #     option_two='option_two',
#         #     option_three='option_three'
#         #     )

#     def test_polllist_not_equal_none(self):
#         result = PollList.get_queryset(self)
#         self.assertIsNotNone(result)

#     # def test_polllist_contains_test_poll(self):
#     #     result = PollList.get_queryset(self)
#     #     poll_object = Poll[0]
#     #     self.assertIn(poll_object, result)

#     def test_get_homepage(self):
#         '''
#         Test to check that the starting page displays
#         Checks:
#         1. status code is 200 (success)
#         and template used is base.html
#         '''
#         c = Client()
#         response = c.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'base.html')

# if __name__ == '__main__':
#     unittest.main()


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)