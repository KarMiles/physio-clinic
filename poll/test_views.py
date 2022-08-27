# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import unittest

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from views import PollList
from blog.views import StaffRequiredMixin


class TestPollList(unittest.TestCase):
    '''
    Should raise a TypeError if...
    '''
    def class_not_equal_none(self):
        result = self.assertTrue(PollList)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()