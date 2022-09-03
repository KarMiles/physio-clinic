# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.contrib.auth import get_user_model
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post, Comment

User = get_user_model()

class TestBlogModels(unittest.TestCase):
    '''
    Test Post model
    '''

    # TESTS SETUP

    @classmethod
    def setUpClass(cls):
        '''
        Class method used for operations carried
        before all tests
        '''
        print('\nTest_models starting')
    
    @classmethod
    def tearDownClass(cls):
        '''
        Class method used for operations carried
        after all tests
        '''
        print('\nTest_models complete')
    
    def setUp(self):
        '''
        Create test data
        '''
        # Create test user
        self.user = User(
            username='TestUser',
            email='test@mail.com',
            password='1qazcde3',
            is_staff='True'
        )

        # Create test post
        self.post = Post(
            title='Ttitle',
            slug='tslug',
            author=self.user,
            content='tcontent',
            excerpt='texcerpt',
            price='tprice',
            priority='3 - Normal',
            status='0'
        )

        # Create test comment
        self.comment = Comment(
            post=self.post,
            author='TCommentAuthor',
            body="tbody",
            approved=True
        )

    # TESTS
    
    def test_create_post(self):
        '''
        Tests that post can be created using Post model
        Checks:
        1. test post is an instance of Post model 
        '''
        self.assertIsInstance(self.post, Post)

    def test_create_post_str_representation(self):
        '''
        Tests string representation for Post model
        Checks:
        1. string representation is equal to post title
        '''
        self.assertEquals(str(self.post), 'Ttitle')

    def test_create_comment(self):
        '''
        Tests that comment can be created using Comment model
        Checks:
        1. test comment is an instance of Comment model 
        '''
        self.assertIsInstance(self.comment, Comment)

    def test_create_comment_str_representation(self):
        '''
        Tests string representation for Comment model
        Checks:
        1. test string representation corresponds to 
        string representation defined in Comment model
        '''
        self.assertEquals(str(self.comment), 'Comment by TCommentAuthor')

    def test_post_image_defaults_to_placeholder(self):
        '''
        Tests that when no image is uploaded image defaults to placeholder
        '''
        self.assertEqual(self.post.featured_image, 'placeholder')