"""A common base test case for re-using."""

import time

from django.test.testcases import LiveServerTestCase
from selenium import webdriver

from issue_tracker import utils


class CommonLiveServerTestCase(LiveServerTestCase):
    """Common methods for all tests."""

    DEFAULT_PAUSE_TIME = 5

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.user_name = 'username'
        self.user_pw = 'usernamepw'
        self.super_user_name = 'test'
        self.super_user_pw = 'testpw'


    def tearDown(self):
        self.driver.quit()
        utils.wipe_db()

    def pause(self, seconds=None):
        """Time to pause between clicks.

        Args:
          seconds: The number of seconds to pause.
        """
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.DEFAULT_PAUSE_TIME)
