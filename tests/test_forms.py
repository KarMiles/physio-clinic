# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.forms import PostForm, CommentForm
from blog.models import Post


# USER SETUP
User = get_user_model()
client = Client()

username_customer = 'test_user_customer'
username_staff = 'test_user_staff'
password = '1qazcde3'

# Login user (customer)
def login_customer():
    client.force_login(
        User.objects.get_or_create(
            username=username_customer,
            password=password,
            is_staff='False'
            )[0])

# Login user (staff)
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


class TestPostForm(unittest.TestCase):
    '''
    This class is for testing Post form
    '''
    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Set up test data used 
        for all tests in TestViews class
        '''
        print('\nTest_views starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Delete test data used 
        for all tests in TestViews class
        '''
        print('\nTest_views complete')
    
    def setUp(self):
        '''
        Set up testing data
        '''
        pass

    def tearDown(self):
        '''
        Delete test data
        '''
        pass
    
    # TESTS

    # def test_user_can_login(self):
    #     """
    #     Tests that user can login.
    #     Checks:
    #     1. that the client session is in allauth registry.
    #     """
    #     login_staff()
    #     self.assertIn('_auth_user_id', client.session)
    #     if '_auth_user_id' in client.session:
    #         print('\nUser can log in')
    #     logout()

    def test_post_title_is_required(self):
        '''
        Tests if the field 'title' is required
        Checks:
        1. form is not valid if title is blank
        2. there is an error message when field is empty
        3. default comment shows

        '''
        form = PostForm({
            'title': '',
            'slug': 'ttitle',
            'author': 'tauthor',
            'content': 'tcontent',
            'excerpt': 'texcerpt',
            'price': 'tprice',
            'priority': '3 - Normal',
            'status': '1'
        })

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        
    def test_post_title_is_required_filled(self):
        '''
        Tests if form with field 'title' containing characters 
        is valid
        Checks:
        1. form is valid if title contains characters
        '''
        form = PostForm({
            'title': 'Ttitle',
            'slug': 'ttitle',
            'author': 'tauthor',
            'content': 'tcontent',
            'excerpt': 'texcerpt',
            'price': 'tprice',
            'priority': '3 - Normal',
            'status': '1'
        })

        self.assertTrue(form.is_valid())
