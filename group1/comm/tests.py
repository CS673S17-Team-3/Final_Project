from django.test import TestCase
from comm.models import Message, Room
from datetime import datetime
from django.contrib.auth.models import User
# Create your tests here.




class MessageLengthTest(TestCase):
	def create_group(self):
		#set up group and User test
		Room.objects.create(name="test", description="maxLength")
		testRoom=room.objects.get("test")

        User.objects.create(password = "1234", last_login = "2017-02-12 21:36:33.211421", is_superuser = 1, username = "test", first_name = "", last_name = "", email = "test1@bu.edu", is_staff = 1, is_active = 1, date_joined = "2017-02-12 21:36:33.211421")

#test
    def add_char(a):
    	while