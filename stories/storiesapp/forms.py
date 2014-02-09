from django import forms
from storiesapp.models import Story, Photo
from django.utils import timezone

class StoryForm(forms.ModelForm):
	author = forms.CharField(max_length=200, help_text="What is your name?")
	title = forms.CharField(max_length=200, help_text="What is your story called?")
	pub_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())

	class Meta:
		model = Story

class PhotoForm(forms.ModelForm):
	caption = forms.CharField(max_length=200, help_text="Caption your moment.")
	pub_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())

	class Meta:
		model = Photo
		fields = ('caption',)