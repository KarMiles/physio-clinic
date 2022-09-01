# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.test import Client
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib import auth

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from poll.views import PollList
from poll.models import Poll


# USER SETUP
User = get_user_model()
client = Client()

username_customer='test_user_customer'
username_staff='test_user_staff'
password='1qazcde3'

# Login user
def login_customer():
    client.force_login(
        User.objects.get_or_create(
            username=username_customer,
            password=password,
            is_staff='False'
            )[0])

def login_staff():
    client.force_login(
        User.objects.get_or_create(
            username=username_staff,
            password=password,
            is_staff='True'
            )[0])
        
# Logout user
def logout():
    client.logout()


class TestViews(unittest.TestCase):
    '''
    Test view to show page with a list of polls
    '''

    # TESTS SETUP
    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used 
        for all tests in TestViews class
        '''
        print('\nsetUpClass')
        
        # Create test user
        if not User.objects.filter(username=username_customer).exists():
            user_customer=User.objects.create(
                username=username_customer,
                password=password,
                is_staff='False'
            )
            print(f'Test user "{user_customer.username}" created.')
        elif not User.objects.filter(username=username_staff).exists():
            user_staff=User.objects.create(
                username=username_staff,
                password=password,
                is_staff='True'
            )
            print(f'Test user "{user_staff.username}" created.')

        else:
            print('Test user already exists, proceeding with test.')

        # logged_in = client.login(
        #     username=username,
        #     password=password)
        # if logged_in:
        #     print('Test user logged in.')
        # else:
        #     print('Test user NOT logged in.')
        
    @classmethod
    def tearDownClass(cls):
        '''
        Delete test data used 
        for all tests in TestViews class
        '''
        print('\ntearDownClass')
        # Delete test user
        User.objects.filter(username=username_customer).delete()
        User.objects.filter(username=username_staff).delete()
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
    
    # TESTS

    def test_user_can_login(self):
        login_customer()
        self.assertIn('_auth_user_id', client.session)
        logout()
    # self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

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
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

        # Polls page loads correctly
        response = client.get('/poll/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/poll_home.html')

        # Login page loads correctly
        response = client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        # Contact page loads correctly
        response = client.get('/contact/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'django_contact_form/contact_form.html')

        # Booking page loads correctly
        login_customer()
        response = client.get('/booking/booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'booking.html')
        logout()

if __name__ == '__main__':
    unittest.main()
