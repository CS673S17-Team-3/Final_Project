import time
from datetime import datetime

from django.contrib.auth.models import User
from comm.models import Room, Message
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.testcases import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CommonLiveServerTestCase(StaticLiveServerTestCase):
	"""Common methods for all tests."""

	DEFAULT_PAUSE_TIME = 5

	def setUp(self):

		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(5)
		self.user_name = 'test'
		self.user_pw = 'Password123'
		user = User.objects.create_superuser(self.user_name, email='%s@bu.edu' % self.user_name, password=self.user_pw, **{'first_name': 'Frodo', 'last_name': 'Baggins'})
		user.save()

		room = Room.objects.create(name="Test", description="maxLength", creator=user)
		room.save()

		message = Message.objects.create(text = "test: Hello", time = datetime.now().time(), room = room, user = user, at_message = False)
		message.save()

	def log_in(self):
		self.driver.get('http://127.0.0.1:8000/communication/')
		self.pause(2)

		self.driver.find_element_by_id('username').send_keys(self.user_name)
		self.driver.find_element_by_id('password').send_keys(self.user_pw)
		self.driver.find_element_by_id('password').send_keys(Keys.ENTER)
		self.pause(2)

		self.driver.get('http://127.0.0.1:8000/communication/')
		self.pause()

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
