from django.db import models

class Story(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")

	def __unicode__(self):
		return self.title

class Photo(models.Model):
	story = models.ForeignKey(Story)
	position = models.IntegerField(default=0)
	caption = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")

	def __unicode__(self):
		return self.caption