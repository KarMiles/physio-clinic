# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.test import Client
from django.views import generic
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from poll.views import PollList
from poll.models import Poll


User = get_user_model()

class TestViews(unittest.TestCase):
    '''
    Test view to show page with a list of polls
    '''
    def setUp(self):
        '''
        Set up testing data
        '''
        # Create test user
        if not User.objects.filter(username='user_staff_test').exists():
            User.objects.create(
                username='user_staff_test',
                password='1qazcde3',
                is_staff='True'
            )
            print('Test user created.')
        else:
            print('Test user already exists, proceeding with test.')

        # Create test Poll
        # Poll.objects.create(
        #     poll_id='999',
        #     author=User.username,
        #     question='Which option?',
        #     option_one='option_one',
        #     option_two='option_two',
        #     option_three='option_three'
        #     )

    def tearDown(self):
        '''
        Delete test data
        '''
        # Delete test user
        User.objects.filter(username='user_staff_test').delete()

    def test_polllist_not_equal_none(self):
        result = PollList.get_queryset(self)
        self.assertIsNotNone(result)

    # def test_polllist_contains_test_poll(self):
    #     result = PollList.get_queryset(self)
    #     poll_object = Poll[0]
    #     self.assertIn(poll_object, result)

    def assertTemplateUsed(self, response, template_name):
            self.assertIn(
                template_name,
                [t.name for t in response.templates if t.name is not None]
            )

    def test_get_page(self):
        '''
        Test to check that the starting page displays
        Checks:
        1. status code is 200 (success)
        and template used is base.html
        '''
        c = Client()

        # Home page
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

        # Polls
        response = c.get('/poll/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/poll_home.html')

        # Login
        response = c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

if __name__ == '__main__':
    unittest.main()
