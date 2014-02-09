from django.conf.urls import patterns, url
from storiesapp import views

urlpatterns = patterns('',
			url(r'^$', views.index, name='index'),
			url(r'^login/$', views.user_login, name='user_login'),
			url(r'^register/$', views.register, name='register'),
			url(r'^add_story/$', views.add_story, name='add_story'),
			url(r'^home/$', views.home, name='home'),
			url(r'^logout/$', views.user_logout, name='user_logout'))