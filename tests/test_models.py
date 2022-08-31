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

        # Create test user
        # if not User.objects.filter(username='user_staff_test').exists():
        #     User.objects.create(
        #         username='user_staff_test',
        #         email='test@mail.com',
        #         password='1qazcde3',
        #         is_staff='True'
        #     )
        #     print('Test user created.')
        # else:
        #     print('Test user already exists, proceeding with test.')

        # Create test post
        self.post = Post(
            title='Ttitle',
            slug='tslug',
            author=self.user,
            content='tcontent',
            excerpt='texcerpt',
            price='tprice',
            priority='3 - Normal',
            status='0',
            created_on='31/08/2022 10:42',
            updated_on='31/08/2022 11:42',
            # TODO Test likes 
            # likes=User.objects.get(pk=id)
        )

        # Create test comment
        self.comment = Comment(
            post=self.post,
            author='TCommentAuthor',
            body="tbody",
            created_on='31/08/2022 10:42',
            approved=True
        )
    
    def test_create_post(self):
        self.assertIsInstance(self.post, Post)

    def test_create_post_str_representation(self):
        self.assertEquals(str(self.post), 'Ttitle')

    def test_create_comment(self):
        self.assertIsInstance(self.comment, Comment)

    def test_create_comment_str_representation(self):
        self.assertEquals(str(self.comment), 'Comment by TCommentAuthor')
