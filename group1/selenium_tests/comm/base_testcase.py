import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.testcases import LiveServerTestCase
from selenium import webdriver

class CommonLiveServerTestCase(StaticLiveServerTestCase):
    """Common methods for all tests."""

    DEFAULT_PAUSE_TIME = 5

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.user_name = 'test'
        self.user_pw = '1234'
        User.objects.create(password = user_pw, last_login = "2017-02-12 21:36:33.211421", is_superuser = 1, username = user_name, first_name = "", last_name = "", email = "test1@bu.edu", is_staff = 1, is_active = 1, date_joined = "2017-02-12 21:36:33.211421")

    def tearDown(self):
        self.driver.quit()
        User.objects.all().delete()

    def pause(self, seconds=None):
    """Time to pause between clicks.

    Args:
      seconds: The number of seconds to pause.
    """
    if seconds:
        time.sleep(seconds)
    else:
        time.sleep(self.DEFAULT_PAUSE_TIME)
