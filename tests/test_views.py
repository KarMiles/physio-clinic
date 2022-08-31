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
c = Client()

class TestViews(unittest.TestCase):
    '''
    Test view to show page with a list of polls
    '''

    @classmethod
    def setUpClass(cls):
        print('\nsetUpClass')
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

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')
        # Delete test user
        User.objects.filter(username='user_staff_test').delete()
        print('Test user deleted.')
    
    def setUp(self):
        '''
        Set up testing data
        '''
        pass
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
        pass

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
        Test to check that the correct page displays.
        Checks:
        1. status code is 200 (success)
        and template used as expected.
        '''
        

        # Home page loads correctly 
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

        # Polls page loads correctly
        response = c.get('/poll/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/poll_home.html')

        # Login page loads correctly
        response = c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        # Contact page loads correctly
        # response = c.get('/contact/contact/')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(
        #     response,
        #     'django_contact_form/contact_form.html')

if __name__ == '__main__':
    unittest.main()
