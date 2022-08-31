# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.contrib.auth import get_user_model
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post

User = get_user_model()

class TestPostModel(unittest.TestCase):
    '''
    Test Post model
    '''
    def setUp(self):
        '''
        Create test user and test post
        '''
        
        self.a = User(
            username='TestUser'
        )

        self.l = User(
            id=User.objects.filter(username='TestUser')
        )

        self.p = Post(
            title='Ttitle',
            slug='tslug',
            author=self.a,
            content='tcontent',
            excerpt='texcerpt',
            price='tprice',
            priority='3 - Normal',
            status='0',
            created_on='31/08/2022 10:42',
            updated_on='31/08/2022 11:42',
            likes=self.l
        )
    
    def test_create_post(self):
        self.assertIsInstance(self.p, Post)

    def test_str_representation(self):
        self.assertEquals(str(self.p), 'Ttitle')