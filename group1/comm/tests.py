from django.test import TestCase
from comm.models import Message, Room
from datetime import datetime
from django.contrib.auth.models import User

# Create your tests here.
class MaxMessagesTestCase(TestCase):
    def setUp(self):
    	#Create room and user objects
        Room.objects.create(name = "test1", description = "test1")
        room1 = Room.objects.get(name = "test1")
        Room.objects.create(name = "test2", description = "test2")
        room2 = Room.objects.get(name = "test2")

        User.objects.create(password = "test1", last_login = "2017-02-12 21:36:33.211421", is_superuser = 1, username = "test1", first_name = "", last_name = "", email = "test1@bu.edu", is_staff = 1, is_active = 1, date_joined = "2017-02-12 21:36:33.211421")
        user = User.objects.get(id = 1);

        #Add 5,100 messages from each room
        for num in range(0, 5100):
            Message.objects.create(text = num, time = datetime.now().time(), room = room1, user = user, at_message = False)
            Message.objects.create(text = num, time = datetime.now().time(), room = room2, user = user, at_message = False)

    def test_count_equal_5000(self):
        room1 = Room.objects.get(name = "test1")
        room2 = Room.objects.get(name = "test2")

        #Check if each room has 5,000 messages and table has 10,000 overall 
        self.assertEqual(Message.objects.filter(room = room1).count(), 5000)
        self.assertEqual(Message.objects.filter(room = room2).count(), 5000)
        self.assertEqual(Message.objects.count(), 10000)