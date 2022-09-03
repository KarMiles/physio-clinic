# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.forms import PostForm


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
        print('\nTest_forms starting')

    @classmethod
    def tearDownClass(cls):
        '''
        Delete test data used 
        for all tests in TestViews class
        '''
        print('\nTest_forms complete')
    
    # TESTS

    def test_post_title_is_required(self):
        '''
        Tests if the field 'title' is required.
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
        is valid.
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

    def test_excerpt_is_not_required(self):
        '''
        Tests that field 'excerpt' is not required.
        Checks:
        1. form is valid if 'excerpt' field is left blank
        '''
        form = PostForm({
            'title': 'Ttitle',
            'slug': 'ttitle',
            'author': 'tauthor',
            'content': 'tcontent',
            'excerpt': '',
            'price': 'tprice',
            'priority': '3 - Normal',
            'status': '1'
        })

        self.assertTrue(form.is_valid())
        
    def test_postform_fields_are_explicit_in_form_metaclass(self):
        """
        Tests that only fields in Meta class desplay in form.
        Checks:
        1. Fields listed in Meta class
        """
        form = PostForm()
        
        self.assertEqual(form.Meta.fields, 
            ('title',
            'content',
            'excerpt',
            'price',
            'featured_image',
            'priority',
            'status',))