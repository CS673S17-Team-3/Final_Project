from django.conf.urls import patterns, url, include
from comm import views

urlpatterns = patterns('',
	url(r'^sendinviteemail/(?P<emailTo>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 
   views.sendInviteEmail, name = 'sendInviteEmail'),
	#url(r'^users/(?P<user_id>\d+)/$', views.test, name ='test'),
    url(r'^$', views.index, name='index'),
)
