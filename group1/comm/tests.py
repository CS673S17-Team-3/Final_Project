from django.test import TestCase
from comm.models import Message, Room
from datetime import datetime
from django.contrib.auth.models import User
# Create your tests here.



class MessageLengthTest(TestCase):
	def setUp(self):
		#set up group and User test
		Room.objects.create(name="test", description="maxLength")
		testRoom=Room.objects.get(name = "test")

		User.objects.create(password = "1234", last_login = "2017-02-12 21:36:33.211421", is_superuser = 1, username = "test", first_name = "", last_name = "", email = "test1@bu.edu", is_staff = 1, is_active = 1, date_joined = "2017-02-12 21:36:33.211421")

#test
	def test_add_char(self):
		message = ""
		for i in range(0,100000000):
			message += "a"

		Message.objects.create(text = message, time = datetime.now().time(), at_message = 0, room = Room.objects.get(name = "test"), user = User.objects.get(id=1) )
		self.assertEqual(Message.objects.count(),1)