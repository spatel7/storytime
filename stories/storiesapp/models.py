from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")

	def __unicode__(self):
		return self.title

class Photo(models.Model):
	story = models.ForeignKey(Story)
	picture = models.ImageField(upload_to='pictures')
	position = models.IntegerField(default=0)
	caption = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")

	def __unicode__(self):
		return self.caption

class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.CharField(max_length=200, blank=True)

	def __unicode__(self):
		return self.user.username