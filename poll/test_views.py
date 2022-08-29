# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest
from django.views import generic
from django.contrib.auth import get_user_model

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from poll.views import PollList
from poll.models import Poll


User = get_user_model()

class TestPoll(unittest.TestCase):
    '''
    Test view to show page with a list of polls
    '''
    def setUp(self):
        '''
        Set up testing data
        '''
        if 'user_staff' not in User.objects.all():
            user_staff = User.objects.create_user(
                username='user_staff',
                password='1qazcde3',
                is_staff='True'
            )

        Poll.objects.create(
            poll_id='1',
            author=user_staff.username,
            question='Which option?',
            option_one='option_one',
            option_two='option_two',
            option_three='option_three'
            )

        # pass


    def tearDown(self):
        '''
        Delete test data
        '''
        # User.objects[-1].delete()
        # Poll.objects[-1].delete()

    def test_polllist_not_equal_none(self):
        result = PollList.get_queryset(self)
        print(result)
        self.assertIsNotNone(result)

    # def test_polllist_is_a_list(self):
    #     result = PollList.get_queryset(self)
    #     self.

    def test_polllist_contains_test_poll(self):
        result = PollList.get_queryset(self)
        poll_object = Poll[0]
        self.assertIn(poll_object, result)


if __name__ == '__main__':
    unittest.main()
