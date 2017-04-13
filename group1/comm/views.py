import django_filters
from django.shortcuts import render
from django.http import HttpResponse
from comm.models import User, Room, Message, UserRoom
from rest_framework import viewsets, generics, filters
from comm.serializers import UserSerializer, RoomSerializer, MessageSerializer, MessageDataSerializer, UserRoomSerializer, UserRoomDataSerializer
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random

# Return the main chat room
@login_required(login_url='/signin')
def index(request):
	context = {'user': request.user}
	return render(request, 'comm/index.html', context)

#a test view
#@login_required(login_url='/signin')
#def test(request):
#	context = {'user': request.user}
#	return render(request, 'com/index.html', context)

#send invite email
@login_required(login_url='/signin')
def sendInviteEmail(request, emailTo):
	res = send_mail("Invite to join room", "hello, you are invited to join the room : ", "testcs673s17@gmail.com", [emailTo])
	return HttpResponse('%s'%res)



## Django REST framework classes...
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer
	def put(self, request):
		id = int(request.data.get("id", "0"))
		name = request.data.get("name", "0")
		room = Room.objects.get(pk=id)
		room.name = name
		room.save()
	def delete(self, request):
		id = int(request.data.get("id", "0"))
		room = Room.objects.get(pk=id)
		room.delete()

class MessageFilter(django_filters.FilterSet):
	user = django_filters.CharFilter(name="user__name")
	room = django_filters.CharFilter(name="room__name")
	class Meta:
		model = Message
		fields = ['user', 'room']

class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all().order_by('time')
	serializer_class = MessageSerializer
	filter_class = MessageFilter

class MessageDataViewSet(viewsets.ReadOnlyModelViewSet):
	# This viewset will show all of the messages in the message model 
	# and all of the data associated with those messages.  The data from
	# the models User and Room will be displayed.
	queryset = Message.objects.all().order_by('time')
	serializer_class = MessageDataSerializer
	filter_class = MessageFilter

class UserRoomFilter(django_filters.FilterSet):
	user = django_filters.CharFilter(name="user__name")
	room = django_filters.CharFilter(name="room__name")
	class Meta:
		model = UserRoom
		fields = ['user', 'room']

class UserRoomViewSet(viewsets.ModelViewSet):
	queryset = UserRoom.objects.all()
	serializer_class = UserRoomSerializer
	filter_class = UserRoomFilter

class UserRoomDataViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = UserRoom.objects.all()
	serializer_class = UserRoomDataSerializer
	filter_class = UserRoomFilter

class MessageSearchSet(viewsets.ReadOnlyModelViewSet):
	queryset=Message.objects.all().order_by('time')
	serializer_class=MessageDataSerializer
  	filter_backends=(filters.SearchFilter,)
	search_fields=('text','time')
