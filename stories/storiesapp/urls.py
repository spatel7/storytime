from django.conf.urls import patterns, url
from storiesapp import views

urlpatterns = patterns('',
			url(r'^$', views.index, name='index'),
			url(r'^login/', views.login, name='login'),
			url(r'^register/', views.register, name='register'),
			url(r'^add_story/$', views.add_story, name='add_story'))